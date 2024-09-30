# Create the Flask application instance
from flask import Flask
# Import necessary modules
from flask import Flask, render_template, redirect, url_for, flash, request, session
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from models.user import User
from utils.captcha import validate_captcha
from utils.security import verify_password_strength, hash_password, check_password

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Load configuration from the config.py file
app.config.from_object('config.Config')

# Initialize the database and other extensions
db = SQLAlchemy(app)  # Database instance
bcrypt = Bcrypt(app)  # Password hashing
login_manager = LoginManager(app)  # User session management
login_manager.login_view = 'login'  # Redirect to login page if unauthorized

# Load User from Database for LoginManager
@login_manager.user_loader
def load_user(user_id):
    """Load a user from the database by ID for session management."""
    return User.query.get(int(user_id))

# Define the registration form
class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    captcha = StringField('Captcha', validators=[DataRequired()])
    submit = SubmitField('Register')

# Define the login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    captcha = StringField('Captcha', validators=[DataRequired()])
    submit = SubmitField('Login')

# Home Page Route
@app.route('/')
def index():
    """Render the home page."""
    return render_template('dashboard.html')

# About Us Page Route
@app.route('/about-us')
def about_us():
    """Render the About Us page."""
    return render_template('profile.html')

# Dashboard Route (requires login)
@app.route('/dashboard')
@login_required
def dashboard():
    """Render the dashboard page for logged-in users."""
    return render_template('dashboard.html')

# User Profile Route (requires login)
@app.route('/profile')
@login_required
def profile():
    """Render the profile page showing user details."""
    return render_template('profile.html')

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Handle user registration."""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Check password strength
        if not verify_password_strength(form.password.data):
            flash('Password does not meet strength requirements', 'danger')
            return redirect(url_for('register'))

        # Validate CAPTCHA
        if not validate_captcha(form.captcha.data):
            flash('CAPTCHA validation failed', 'danger')
            return redirect(url_for('register'))

        # Hash the password and create a new user
        hashed_password = hash_password(form.password.data)
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)  # Add the user to the session
        db.session.commit()    # Commit changes to the database
        flash('Account created successfully. Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# User Login Route
def send_otp(email):
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    form = LoginForm()
    if form.validate_on_submit():
        # Check if user exists and validate password
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password(user.password, form.password.data):
            # Validate CAPTCHA
            if not validate_captcha(form.captcha.data):
                flash('CAPTCHA validation failed', 'danger')
                return redirect(url_for('login'))

            login_user(user)  # Log the user in
            session['mfa_verified'] = False  # Reset MFA verification
            send_otp(user.email)  # Send OTP for MFA
            flash('An OTP has been sent to your email for verification.', 'info')
            return redirect(url_for('verify_mfa'))  # Redirect to MFA verification page

        flash('Login failed. Check email and password.',)
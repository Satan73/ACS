from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from datetime import datetime

# Initialize the database object
db = SQLAlchemy()

class User(db.Model):
    """
    User model represents the user table in the database.
    It stores user information such as name, email, password, address, and role.
    """
    __tablename__ = 'users'  # Define the name of the table

    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each user
    name = db.Column(db.String(100), nullable=False)  # User's name
    email = db.Column(db.String(120), unique=True, nullable=False)  # User's email (must be unique)
    password_hash = db.Column(db.String(128), nullable=False)  # Hashed password
    address = db.Column(db.String(255))  # User's address
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp when the user is created
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))  # Foreign key to the roles table

    role = relationship('Role', back_populates='users')  # Define relationship with Role

    def __repr__(self):
        return f"<User {self.name}, Email: {self.email}>"


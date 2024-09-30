from flask_bcrypt import Bcrypt
from itsdangerous import URLSafeTimedSerializer
from flask import current_app
import random
import string

bcrypt = Bcrypt()

# Hash a password
def hash_password(password):
    """
    Hashes a plaintext password using Bcrypt for secure storage.

    :param password: The plaintext password to hash
    :return: The hashed password
    """
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Check if the entered password matches the stored hash
def check_password(hashed_password, plain_password):
    """
    Verifies if the hashed password matches the plain text password.

    :param hashed_password: The stored hashed password
    :param plain_password: The plaintext password provided by the user
    :return: Boolean indicating whether the password is correct
    """
    return bcrypt.check_password_hash(hashed_password, plain_password)

# Generate a unique token for email verification or password reset
def generate_token(email):
    """
    Generates a unique token for the given email using a URLSafeTimedSerializer.
    This can be used for MFA, email verification, or password reset.

    :param email: The email address for which the token is generated
    :return: A time-sensitive token string
    """
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

# Verify the token and return the associated email
def verify_token(token, expiration=3600):
    """
    Verifies a time-sensitive token and returns the associated email if valid.

    :param token: The token string to verify
    :param expiration: The validity period for the token in seconds (default is 1 hour)
    :return: The email associated with the token if valid"""


def verify_password_strength():
    return None
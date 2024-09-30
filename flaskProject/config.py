import os


class Config:
    """
    Base configuration class that holds default settings for the Flask app.
    These settings will be used in both development and production environments.
    """

    # Secret Key for securely signing session cookies and CSRF protection
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_super_secret_key_that_should_be_changed_in_production'

    # SQLite database configuration - used for local development
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/app.db'

    # Disable SQLAlchemy track modifications to reduce overhead
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ReCAPTCHA Public and Private Keys for CAPTCHA validation
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'your_recaptcha_public_key'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'your_recaptcha_private_key'

    # Email configuration for sending OTPs or password reset links (using a sample SMTP server)
    MAIL_SERVER = 'smtp.gmail.com'  # Change this for your actual email provider
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'your-email@gmail.com'  # Placeholder
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'your-email-password'  # Placeholder

    # Security features: session timeout, HTTPS enforcement, etc.
    REMEMBER_COOKIE_DURATION = 60 * 60 * 24 * 7  # Remember user session for one week
    SESSION_COOKIE_SECURE = True  # Ensures the session cookie is only sent over HTTPS
    WTF_CSRF_TIME_LIMIT = None  # CSRF protection with no expiration limit

    # MFA settings (time-based one-time password validity)
    MFA_TOKEN_EXPIRY = 300  # OTP (One-Time Password) expiry time in seconds (5 minutes)

    # CAPTCHA image settings (if not using Google reCAPTCHA)
    CAPTCHA_FOLDER = os.path.join('assets', 'captchas')  # Folder to store CAPTCHA images
    CAPTCHA_FONT_PATH = os.path.join('static', 'fonts', 'captcha_font.ttf')  # Font for CAPTCHA text

    # Logging configuration (optional)
    LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL') or 'DEBUG'  # Adjust logging level for production


class DevelopmentConfig(Config):
    """
    Development-specific configuration. Inherits from Config.
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True  # Logs SQL queries for debugging


class ProductionConfig(Config):
    """
    Production-specific configuration. Inherits from Config.
    Override specific settings for production environment.
    """

    DEBUG = False
    SQLALCHEMY_ECHO = False  # Disable SQL query logging in production
    SESSION_COOKIE_SECURE = True  # Force HTTPS in production


class TestingConfig(Config):
    """
    Testing-specific configuration. Inherits from Config.
    Used when running unit tests.
    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_app.db'  # Use a separate test database
    WTF_CSRF_ENABLED = False  # Disable CSRF for testing purposes
    SESSION_COOKIE_SECURE = False  # Disable HTTPS requirement for tests

import re


def verify_password_strength(password):
    """
    Verifies the strength of the password by checking if it meets various security criteria:
    - Minimum 8 characters
    - Contains at least one lowercase letter
    - Contains at least one uppercase letter
    - Contains at least one digit
    - Contains at least one special character

    :param password: The password string to validate
    :return: Boolean indicating if the password meets the strength requirements
    """
    if len(password) < 8:
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[0-9]', password):
        return False
    if not re.search(r'[@$!%*?&]', password):
        return False

    return True


def check_password_match(password, confirm_password):
    """
    Checks if the password and confirm password fields match.

    :param password: The password string
    :param confirm_password: The confirmation password string
    :return: Boolean indicating if the passwords match
    """
    return password == confirm_password

import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
from flask import session
from io import BytesIO

# Generate a random CAPTCHA string
def generate_captcha(length=6):
    """
    Generates a random CAPTCHA string of the given length using letters and digits.
    The generated CAPTCHA is stored in the session for later validation.

    :param length: Number of characters in the CAPTCHA (default is 6)
    :return: The generated CAPTCHA string
    """
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(length))
    session['captcha_text'] = captcha_text  # Store CAPTCHA in session for validation
    return captcha_text

# Create CAPTCHA image
def create_captcha_image(text):
    """
    Creates a CAPTCHA image using the given text.
    The image is generated using the Pillow (PIL) library and saved in a BytesIO buffer.

    :param text: CAPTCHA text to display in the image
    :return: BytesIO object containing the generated CAPTCHA image
    """
    img_width, img_height = 150, 50  # Image size
    font_path = os.path.join('static', 'fonts', 'captcha_font.ttf')  # Path to CAPTCHA font
    font = ImageFont.truetype(font_path, 40)

    # Create a blank image with white background
    image = Image.new('RGB', (img_width, img_height), color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    # Draw CAPTCHA text in random positions
    for i, char in enumerate(text):
        draw.text((10 + i * 25, 5), char, font=font, fill=(0, 0, 0))

    # Add some noise or distortions (optional for extra security)
    draw.line([(random.randint(0, img_width), random.randint(0, img_height)) for _ in range(5)], fill=(0, 0, 0), width=2)

    # Save image to BytesIO buffer
    image_buffer = BytesIO()
    image.save(image_buffer, 'PNG')
    image_buffer.seek(0)

    return image_buffer

# Validate the entered CAPTCHA against the one stored in the session
def validate_captcha(user_input):
    """
    Validates the CAPTCHA entered by the user against the one stored in the session.

    :param user_input: The CAPTCHA input provided by the user
    :return: Boolean indicating whether the CAPTCHA is valid
    """
    return session.get('captcha_text', '').lower() == user_input.lower()

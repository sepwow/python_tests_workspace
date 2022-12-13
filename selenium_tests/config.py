import os

from dotenv import load_dotenv


load_dotenv()

valid_email = os.getenv('email')
valid_password = os.getenv('password')
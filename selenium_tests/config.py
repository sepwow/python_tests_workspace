import os

from dotenv import load_dotenv


load_dotenv()

email = os.getenv('email')
password = os.getenv('password')
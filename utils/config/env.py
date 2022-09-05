import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('taxofficemanagement_url')
USE_DOCKER = bool(os.getenv('USE_DOCKER'))
LOGS_DIR = os.getenv('LOGS_DIR')
SCREENSHOT_DIR = os.getenv('SCREENSHOT_DIR')
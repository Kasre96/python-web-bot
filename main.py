from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import os
from dotenv import load_dotenv
from pathlib import Path

# Load env vars
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Initiate browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# Open web page
driver.get('https://twitter.com')

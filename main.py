"""
A web bot that automatically opens the browser, logs into twitter and opens up notifications page
"""
import os
from pathlib import Path
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# Load env vars
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, override=True)

# Load pass and email from env
u_name = os.getenv('USERNAME')
u_pass = os.getenv('PASSWORD')

# chrome driver options
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')

# Initiate browser
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# Open web page
driver.get('https://twitter.com')

# Find username and password fields and fill with them with relevant data
username_field = driver.find_element_by_name('session[username_or_email]')
username_field.send_keys(u_name)

password_field = driver.find_element_by_name('session[password]')
password_field.send_keys(u_pass)

# Find login button and click it
login_btn = driver.find_element(By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")
login_btn.click()

# Wait for search field to appear and search for Chelsea FC
search_field = WebDriverWait(driver, 5).until(
    ec.presence_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"))
)
search_field.send_keys('Chelsea FC')
search_field.send_keys(Keys.ENTER)

# Find notifications button and click it
notifications_btn = driver.find_element(By.XPATH, "//a[@data-testid='AppTabBar_Notifications_Link']")
notifications_btn.click()

time.sleep(5)
driver.quit()

import os
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver import get_driver

# load variables from local .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def test_login_success(driver):
    # define a 20 sec of wait until elements are loaded
    wait = WebDriverWait(driver, 20)

    try:
        print("Navigating to home page...")
        driver.get(BASE_URL)

        print("Navigating to login page...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='nav-sign-in']"))).click()

        print("Filling email...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='email']"))).send_keys(EMAIL)

        print("Filling password...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys(PASSWORD)

        print("Clicking login button...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='login-submit']"))).click()

        print("Verifying successful login...")
        wait.until(EC.url_contains("/account"))
        
        print("Verifying account page element...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='page-title']")))

        print("Login successful!")

    except Exception as e:
        # when an exception is thrown, it is documented with a screenshot
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"screenshots/test_login_fail_{timestamp}.png")
        print(f"Test failed: {e}")
        raise e

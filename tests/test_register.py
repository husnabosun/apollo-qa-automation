import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils.driver import get_driver

# load variables from local .env file
load_dotenv()

BASE_URL = os.getenv("BASE_URL" , "https://practicesoftwaretesting.com")

def test_register_success(driver):
    # define a 20 sec of wait until elements are loaded
    wait = WebDriverWait(driver, 20)

    try:
        # creates a unique email adress to register each time succesfully
        unique_email = f"testuser_{uuid.uuid4().hex[:8]}@example.com"
        
        print("Navigating to home page...")
        driver.get(BASE_URL)

        print("Navigating to login page...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='nav-sign-in']"))).click()
        
        print("Navigating to register page...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='register-link']"))).click()

        print("Filling first name...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='first-name']"))).send_keys("Test")

        print("Filling last name...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='last-name']").send_keys("User")

        print("Filling date of birth...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='dob']").send_keys("1990-01-01")

        print("Selecting country...")
        Select(driver.find_element(By.CSS_SELECTOR, "[data-test='country']")).select_by_value("US")

        print("Filling postal code...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='postal_code']").send_keys("12345")

        print("Filling house number...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='house_number']").send_keys("42")

        print("Filling street...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='street']").send_keys("Test Street")

        print("Filling city...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='city']").send_keys("Test City")

        print("Filling state...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='state']").send_keys("Test State")

        print("Filling phone...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='phone']").send_keys("1234567890")

        print("Filling email...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='email']").send_keys(unique_email)

        print("Filling password...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("Apollo@QA2024#!")

        print("Clicking register button...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='register-submit']"))).click()
        
        print("Verifying redirect to login page...")
        
        wait.until(EC.url_contains("/auth/login"))
        print("Registration successful! Redirected to login page.")

    except Exception as e:
        # when an exception is thrown, it is documented with a screenshot
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"screenshots/test_register_fail_{timestamp}.png")
        print(f"Test failed: {e}")
        raise e


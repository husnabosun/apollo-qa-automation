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

# a default url also added in case of a failure in reading of .env
BASE_URL = os.getenv("BASE_URL" , "https://practicesoftwaretesting.com")

def test_add_to_cart(driver):
    # define a 20 sec of wait until elements are loaded
    wait = WebDriverWait(driver, 20)

    try:
        print("Navigating to home page...")
        driver.get(BASE_URL)

        print("Searching for product...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='search-query']"))).send_keys("Combination Pliers")

        print("Clicking search button...")
        driver.find_element(By.CSS_SELECTOR, "[data-test='search-submit']").click()

        print("Clicking on product...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.card"))).click()

        print("Clicking increase quantity...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='increase-quantity']"))).click()

        print("Clicking add to cart...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='add-to-cart']"))).click()
        
        print("Verifying success message...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.toast-success")))
        print("Add to cart successful!")
        
    except Exception as e:
        # when an exception is thrown, it is documented with a screenshot
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"screenshots/test_add_to_cart_fail_{timestamp}.png")
        print(f"Test failed: {e}")
        raise e

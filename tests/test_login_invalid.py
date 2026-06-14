import os
from datetime import datetime
from dotenv import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://practicesoftwaretesting.com")


def test_login_invalid_credentials(driver):
    wait = WebDriverWait(driver, 20)

    try:
        print("Navigating to home page...")
        driver.get(BASE_URL)

        print("Navigating to login page...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='nav-sign-in']"))).click()

        print("Entering invalid credentials...")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='email']"))).send_keys("invalid@example.com")
        driver.find_element(By.CSS_SELECTOR, "[data-test='password']").send_keys("wrongpassword123")

        print("Clicking login button...")
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-test='login-submit']"))).click()

        print("Verifying error message...")
        error = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-test='login-error']")))
        assert error.is_displayed()
        print("Invalid login correctly rejected!")

    except Exception as e:
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        driver.save_screenshot(f"screenshots/test_login_invalid_fail_{timestamp}.png")
        print(f"Test failed: {e}")
        raise e
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

# Start WebDriver
service = Service(ChromeDriverManager().install())  # Creates a Service object
driver = webdriver.Chrome(service=service)  # Uses Service instead of passing a string

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Open the Demoblaze website
driver.get("https://demoblaze.com")

# Click the "Sign up" button from the navigation menu
signup_btn = driver.find_element(By.ID, "signin2")
signup_btn.click()

# Wait for the signup modal to appear
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "signInModal"))
)

# Find the Username, Passowrd and Signup button
username = driver.find_element(By.ID, "sign-username")
password = driver.find_element(By.ID, "sign-password")
signup_confirm = driver.find_element(By.XPATH, "//button[text()='Sign up']")

# Fill in the Username
unique_username = "TestUser" + str(int(time.time()))  
username.send_keys(unique_username)

# Fill in the Password
password.send_keys("TestPass123")

# Click "Sign Up" button on the signup modal
signup_confirm.click()

# Waits for the alert
alert = WebDriverWait(driver, 5).until(EC.alert_is_present())  
alert_text = alert.text

# Assert that the alert is displayed
assert alert is not None, "No alert was displayed!"

# Accept the alert to proceed
alert.accept()

# Assert that the alert contains the expected text
expected_message = "Sign up successful"
assert expected_message in alert_text, f"Unexpected alert message: {alert_text}"
logging.info("✅ Sign up successful!")

# Closer the browser
driver.quit()

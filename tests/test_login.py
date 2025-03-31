from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Start WebDriver
service = Service(ChromeDriverManager().install())  
driver = webdriver.Chrome(service=service)  

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Open the Demoblaze website
driver.get("https://demoblaze.com")

# Click "Log in" button from the navigation menu
login_btn = driver.find_element(By.ID, "login2")
login_btn.click()

# Wait for the login modal to appear
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "logInModal"))
)

# Find the Username, Passowrd and Login button
username = driver.find_element(By.ID, "loginusername")
password = driver.find_element(By.ID, "loginpassword")
login_confirm = driver.find_element(By.XPATH, "//button[text()='Log in']")

# Fill in the Username and Password
test_username = "TestUser235"
test_password = "TestPass235" 
username.send_keys(test_username)
password.send_keys(test_password)

# Click "Log in" button on the login modal
login_confirm.click()

# Wait for the welcome text to be updated
WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.ID, "nameofuser"), "Welcome")
)

# Get the actual welcome text
welcome_element = driver.find_element(By.ID, "nameofuser")
welcome_text = welcome_element.text

# Expected text should contain "Welcome" and the test_username
expected_text = f"Welcome {test_username}" 

# Assert that the welcome text contains "Welcome" and the test_username
assert expected_text in welcome_text, f"Expected '{expected_text}' in text, but got: {welcome_text}"

logging.info(f"✅ Login successful! Welcome text verified: {welcome_text}")

# Close browser
driver.quit()
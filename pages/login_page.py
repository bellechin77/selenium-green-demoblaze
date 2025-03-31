from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from utils.config_reader import ConfigReader
from pages.base_page import BasePage
from utils.constants import TEST_USER_ID
 
class LoginPage(BasePage):   
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        super().__init__(driver, fluent_wait, explicit_wait, logger)
        
        # Locators
        self.login_button = (By.ID, "login2")
        self.modal = (By.ID, "logInModal")
        self.username_field = (By.ID, "loginusername")
        self.password_field = (By.ID, "loginpassword")
        self.confirm_login = (By.XPATH, "//button[text()='Log in']")
        self.welcome_text = (By.ID, "nameofuser")
        
    def login_test_user(self):
        try:
            self.logger.info("Logging in a test user...")
            self.open_login_modal()
            self.enter_credentials()
            self.submit_login()
            self.verify_welcome_text()
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"❌ Login failed: {e}")
            raise

    def open_login_modal(self):
        try:
            self.click(self.login_button)
            self.is_element_visible(self.modal)
        except TimeoutException:
            self.logger.error("❌ Login modal did not appear in time!")
            raise
        
    def enter_credentials(self):  
        try:     
            username = ConfigReader.get_property("test_username") + str(TEST_USER_ID) 
            password = ConfigReader.get_property("test_password") + str(TEST_USER_ID) 
            self.logger.info(f"Entering credentials: {username} / [HIDDEN]") 
        
            # Fills in the login form
            self.enter_text(self.username_field, username)
            self.enter_text(self.password_field, password)
        except TimeoutException:
            self.logger.error("❌ Login fields are not interactable!")
            raise

    def submit_login(self):
        # Clicks the login button
        try:
            self.click(self.confirm_login)
            self.logger.info("✅ Login button clicked.")
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
            self.logger.error(f"❌ Failed to click login button: {e}")
            raise
    
    def get_welcome_text(self):
        try:
            welcome_text = self.get_text(self.welcome_text)
            self.logger.info(f"✅ Welcome text retrieved: {welcome_text}")
            return welcome_text
        except (NoSuchElementException, TimeoutException, StaleElementReferenceException) as e:
            self.logger.error(f"❌ Failed to get welcome text: {e}")
            raise
    
    def verify_welcome_text(self):
        username = ConfigReader.get_property("test_username") + str(TEST_USER_ID) 
        expected_text = f"Welcome {username}"
        try:
            welcome_text = self.get_welcome_text()

            # Assert that the welcome text contains "Welcome" and the test_username
            assert expected_text in welcome_text, f"Expected '{expected_text}' in text, but got: {welcome_text}"
            self.logger.info(f"✅ Login successful! Welcome text verified: {welcome_text}")
        except AssertionError as e:
            self.logger.error(f"❌ Login verification failed: {e}")
            raise
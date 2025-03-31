from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException
from utils.config_reader import ConfigReader
from pages.base_page import BasePage
import uuid

class SignupPage(BasePage):
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        super().__init__(driver, fluent_wait, explicit_wait, logger)
        
        # Locators
        self.signup_button = (By.ID, "signin2")
        self.modal = (By.ID, "signInModal")
        self.username_field = (By.ID, "sign-username")
        self.password_field = (By.ID, "sign-password")
        self.confirm_signup = (By.XPATH, "//button[text()='Sign up']")       
        
    def signup_new_user(self):
        try:
            self.logger.info("Signing up a new user...")
            self.open_signup_modal()
            self.enter_credentials()
            self.submit_signup()
            self.handle_alert()
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f"❌ Signup failed: {e}")
            raise

    def open_signup_modal(self):
        try:
            self.click(self.signup_button)
            self.is_element_visible(self.modal)
        except TimeoutException:
            self.logger.error("❌ Signup modal did not appear in time!")
            raise
        
    def enter_credentials(self):
        try:
            new_username = ConfigReader.get_property("test_username") + str(uuid.uuid4().hex)  
            new_password = ConfigReader.get_property("test_password") + str(uuid.uuid4().hex) 
            self.logger.info(f"Entering credentials: {new_username} / [HIDDEN]") 
        
            # Fills in the signup form
            self.enter_text(self.username_field, new_username)
            self.enter_text(self.password_field, new_password)
        except TimeoutException:
            self.logger.error("❌ Signup fields are not interactable!")
            raise
        
    def submit_signup(self):
        # Clicks the signup button
        try:
            self.logger.info("Submitting signup form...")
            self.click(self.confirm_signup)
            self.explicit_wait.until(EC.alert_is_present())
        except TimeoutException:
            self.logger.error("❌ No alert appeared after signup submission!")
            raise
        
    def handle_alert(self):
        # Handles alert pop-up after signup
        try:
            alert = self.explicit_wait.until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            
            if "Sign up successful" not in alert_text:
                self.logger.warning(f"⚠️ Unexpected alert message: {alert_text}")
                raise AssertionError(f"Unexpected alert message: {alert_text}")
            
            self.logger.info("✅ Signup test passed successfully!")          
        except UnexpectedAlertPresentException:
            self.logger.error("❌ Unexpected alert issue occurred!")
            raise
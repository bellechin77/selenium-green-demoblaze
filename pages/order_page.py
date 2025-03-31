from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from pages.base_page import BasePage

class OrderPage(BasePage):
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        super().__init__(driver, fluent_wait, explicit_wait, logger)
        
        # Locators
        self.place_order_button = (By.XPATH, "//button[text()='Place Order']")
        self.order_modal = (By.ID, "orderModal")        
        self.fields = {
            "name": (By.ID, "name"),
            "country": (By.ID, "country"),
            "city": (By.ID, "city"),
            "card": (By.ID, "card"),
            "month": (By.ID, "month"),
            "year": (By.ID, "year")
        }
        self.purchase_button = (By.XPATH, "//button[text()='Purchase']")
        self.confirmation_text = (By.CLASS_NAME, "sweet-alert")
        self.ok_button = (By.XPATH, "//button[text()='OK']")

    def place_order(self, order_data):
        # Places an order by filling details and verifying confirmation
        try:
            self.logger.info("Placing an order...")
            self.open_order_modal()
            self.fill_order_details(order_data)
            self.submit_order()
            
            self.logger.info("Verifying order confirmation...")
            if not self.verify_confirmation():
                self.logger.warning("⚠️ Purchase confirmation failed!")
                raise AssertionError("❌ Purchase confirmation failed!")
            
            self.logger.info("✅ Purchase confirmed successfully!")
            self.confirm_popup()
        except TimeoutException:
            self.logger.error("❌ Timeout while placing the order!")
            raise
        except NoSuchElementException as e:
            self.logger.error(f"❌ Missing element error: {e}")
            raise
        except WebDriverException as e:
            self.logger.error(f"❌ WebDriver encountered an issue: {e}")
            raise

    def open_order_modal(self):
        # Opens the order modal
        try:
            self.logger.info("Opening the order modal...")
            self.click(self.place_order_button)
            self.explicit_wait.until(EC.visibility_of_element_located(self.order_modal))
            self.logger.info("✅ Order modal opened.")
        except TimeoutException:
            self.logger.error("❌ Timeout while opening the order modal!")
            raise
            
    def fill_order_details(self, order_data):
        # Fills in the order details using provided test data
        try:
            self.logger.info("Filling in order details...")
            for field, value in order_data.items():
                if field in self.fields:
                    self.enter_text(self.fields[field], value)
                else:
                    self.logger.warning(f"⚠️ Unexpected field '{field}' in test data.")
            self.logger.info("✅ Order details entered successfully.")
        except NoSuchElementException as e:
            self.logger.error(f"❌ Unable to fill order details: {e}")
            raise

    def submit_order(self):
        # Submits the order by clicking 'Purchase'
        try:
            self.logger.info("Submitting the order...")
            self.click(self.purchase_button)
                    
            self.logger.info("✅ Order submitted.")
        except TimeoutException:
            self.logger.error("❌ Timeout while submitting the order!")
            raise

    def verify_confirmation(self):
        # Verifies order confirmation message
        try:
            self.logger.info("Checking order confirmation message...")
            confirmation_text = self.get_text(self.confirmation_text)
            return "Thank you for your purchase!" in confirmation_text
        except NoSuchElementException:
            self.logger.error("❌ Confirmation message not found!")
            return False

    def confirm_popup(self):
        # Clicks the OK button in the confirmation popup
        try:
            self.logger.info("Confirming the order popup...")
            self.click(self.ok_button)
            self.logger.info("✅ Order popup confirmed.")
        except TimeoutException:
            self.logger.error("❌ Timeout while confirming the popup!")
            raise
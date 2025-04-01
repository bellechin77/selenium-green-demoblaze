from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    WebDriverException,
    StaleElementReferenceException,
)
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        super().__init__(driver, fluent_wait, explicit_wait, logger)
        
        # Locators
        self.cart_button = (By.ID, "cartur")
        self.cart_items = (By.CSS_SELECTOR, "tbody tr td:nth-child(2)")

    def verify_cart(self, max_retries=3, delay=2):
        # Verifies that the expected products are present in the cart
        try: 
            self.logger.info("Verifying cart contents...")
            self.navigate_to_cart()  
            
            # Fetch the cart products with retry mechanism for empty cart issues
            cart_products = self.get_cart_products_with_retry(max_retries, delay)
            
            # Debugging: log the retrieved cart products
            self.logger.info(f"🛒 Cart contains: {cart_products}")
    
            assert any("Samsung" in p or "Nokia" in p for p in cart_products), "❌ Phone missing"
            assert any("MacBook" in p or "Sony" in p for p in cart_products), "❌ Laptop missing"
            assert "Apple monitor 24" in cart_products, "❌ Monitor not in cart"
            
            self.logger.info("All products correctly added to cart ✅")
        except TimeoutException:
            self.logger.error("❌ Timeout while verifying cart contents!")
            raise
        except AssertionError as e:
            self.logger.warning(f"⚠️ Assertion failed: {e}")
            raise
        except WebDriverException as e:
            self.logger.error(f"❌ WebDriver error encountered: {e}")
            raise
        
    def navigate_to_cart(self):
        # Clicks on the cart button to navigate to the cart page
        try:
            self.logger.info("Navigating to cart...")
            self.click(self.cart_button)
            
            # Refresh cart to ensure all items are loaded
            self.driver.refresh()
            
            # Wait for cart items to be present first
            self.explicit_wait.until(EC.presence_of_element_located(self.cart_items),
                "Cart page did not load in time")
    
            self.logger.info("✅ Successfully navigated to cart with contents loaded.")
        except TimeoutException:
            self.logger.error("❌ Timeout while waiting for cart contents to fully load!")
            raise
        except NoSuchElementException:
            self.logger.error("❌ Cart button not found!")
            raise
                 
    def get_cart_products(self):
        # Retrieves the list of product names from the cart
        try:
            self.logger.info("Retrieving cart products...")
            
            # Ensure at least 2 cart items are present before proceeding
            self.fluent_wait.until(lambda driver: len(driver.find_elements(*self.cart_items)) > 1, 
                "Timeout waiting for multiple cart items")
            cart_items = self.fluent_wait.until(EC.visibility_of_all_elements_located(self.cart_items))
            
             # Re-locate elements if stale
            products = []
            for item in cart_items:
                try:
                    products.append(item.text)
                except StaleElementReferenceException:
                    self.logger.warning("⚠️ Stale element encountered, re-locating cart items...")
                    return self.get_cart_products()  # Re-attempt retrieval

            if not products:
                self.logger.warning("⚠️ Cart appears to be empty!")

            return products
        except TimeoutException:
            self.logger.error("❌ Timeout while retrieving cart products!")
            raise
        except NoSuchElementException:
            self.logger.error("❌ Cart items not found!")
            raise
        except StaleElementReferenceException:
            self.logger.warning("⚠️ Cart items were stale. Retrying...")
            return self.get_cart_products()  # Retry fetching products


    def get_cart_products_with_retry(self, max_retries=3, delay=2):
        # Retries getting cart products using a loop instead of recursion
        for attempt in range(max_retries):
            try:
                return self.get_cart_products()
            except StaleElementReferenceException:
                self.logger.warning(f"⚠️ Stale elements detected. Retrying... ({attempt + 1}/{max_retries})")
            except TimeoutException:
                self.logger.warning(f"⚠️ Cart took too long to load. Retrying... ({attempt + 1}/{max_retries})")

            # Wait dynamically for new elements to appear 
            self.fluent_wait.until(EC.presence_of_all_elements_located(self.cart_items), 
                            message="Waiting for cart items to appear")

        self.logger.error("❌ Cart is empty after multiple retries!")
        raise AssertionError("Cart is empty after retries!")
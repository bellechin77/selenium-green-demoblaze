from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementClickInterceptedException
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        super().__init__(driver, fluent_wait, explicit_wait,logger)
        
        # Locators
        self.category_link = "//a[text()='{category}']"
        self.products = (By.CSS_SELECTOR, ".card-title a")
        self.add_to_cart_button = (By.XPATH, "//a[text()='Add to cart']")
        self.home_button = (By.PARTIAL_LINK_TEXT, "Home")

    def add_product(self, category=None, product_name=None, first=False, last=False):   
        # Selects a product from a given category and adds it to the cart
        if not category:
            raise ValueError("❌ Category cannot be None!")

        try:
            # Click on category
            self.click((By.XPATH, self.category_link.format(category=category)))
            self.logger.info(f"✅ Clicked on category: {category}")

            # Wait for products to appear
            self.fluent_wait.until(EC.presence_of_element_located(self.products))
            self.logger.info("✅ Products loaded successfully!")
        except TimeoutException:
            self.logger.error(f"❌ Products not found for category: {category}")
            raise
    
        # Find product
        product_element = None
        try:
            if product_name:
                self.logger.info(f"Searching for product: {product_name}")
                product_element = self.fluent_wait.until(EC.visibility_of_element_located((By.LINK_TEXT, product_name)))
            else:
                product_list = self.driver.find_elements(*self.products)
                if not product_list:
                    self.logger.warning(f"⚠️ No products found in category: {category}")
                    raise NoSuchElementException(f"No products available in category: {category}")
                
                product_element = product_list[0] if first else product_list[-1] if last else None

            if product_element:
                self.logger.info(f"Clicking on product: {product_element.text}")
                product_element.click()
            else:
                self.logger.warning("⚠️ No product selected")
        except (NoSuchElementException) as e:
            self.logger.error(f"❌ Failed to add product - {str(e)}")
            raise
        
        # Add to cart
        self.add_to_cart_and_accept()
        self.navigate_to_home()
       
    def add_to_cart_and_accept(self):
        # Adds the selected product to the cart and accepts the alert
        try:
            self.logger.info("Clicking 'Add to Cart' button...")
            self.click(self.add_to_cart_button)
            alert = self.explicit_wait.until(EC.alert_is_present())
            alert.accept()
            self.logger.info("✅ Product added to cart successfully!")
        except TimeoutException:
            self.logger.error("❌ Add to cart failed - Alert not found!")
            raise
        except ElementClickInterceptedException:
            self.logger.error("❌ Unable to click 'Add to Cart' button - Blocked by another element!")
            raise
        
    def navigate_to_home(self):
        # Navigates back to the homepage
        try:
            self.logger.info("Navigating back to home...")
            self.click(self.home_button)
            self.fluent_wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".carousel")))
            self.logger.info("✅ Successfull redirected to homepage")
        except TimeoutException:
            self.logger.error("❌ Failed to return to home - Page did not load properly!")
            raise
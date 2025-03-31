from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver, wait, logger):
        super().__init__(driver, wait, logger)

    # Locators
        self.signup_button = (By.ID, "signin2")
        self.login_button = (By.ID, "login2")
        self.logout_button = (By.ID, "logout2")
        self.cart_button = (By.ID, "cartur")
        self.home_button = (By.PARTIAL_LINK_TEXT, "Home")
        self.welcome_text = (By.ID, "nameofuser")
        self.category_link = "//a[text()='{category}']"
        
    def open_home_page(self):
        self.open_url()

    def navigate_to_signup(self):
        self.click(self.signup_button)

    def navigate_to_login(self):
        self.click(self.login_button)

    def navigate_to_cart(self):
        self.click(self.cart_button)
        
    def navigate_to_home(self):
        self.click(self.home_button)
        
    def select_category(self, category):
        self.click(self.category_link(category))

    def verify_logout_button_visible(self):
        return self.is_element_present(self.logout_button)
    
    def get_welcome_text(self):
        return self.get_text(self.welcome_text)

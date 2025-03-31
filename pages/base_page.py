# pages/base_page.py
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.config_reader import ConfigReader

class BasePage:
    """Base class for all pages, providing common WebDriver utilities."""
    
    def __init__(self, driver, fluent_wait, explicit_wait, logger):
        self.driver = driver
        self.fluent_wait = fluent_wait
        self.explicit_wait = explicit_wait
        self.logger = logger 
    
    def open_url(self):
        # Open the base URL
        base_url = ConfigReader.get_property("base_url")
        self.logger.info(f"Opening URL: {base_url}")
        self.driver.get(base_url)
        self.wait_for_page_load()
    
    def click(self, by_locator):
        # Click an element
        element = self.explicit_wait.until(EC.element_to_be_clickable(by_locator))
        self.logger.info(f"Clicking on element: {by_locator}")
        element.click()
    
    def enter_text(self, by_locator, text):
        # Enter text into an input field
        element = self.explicit_wait.until(EC.visibility_of_element_located(by_locator))
        element.clear()
        element.send_keys(text)
        self.logger.info(f"Entered text '{text}' in field: {by_locator}")
    
    def get_text(self, by_locator):
        # Retrieve text from an element
        element = self.explicit_wait.until(EC.visibility_of_element_located(by_locator))
        text = element.text
        self.logger.info(f"Retrieved text '{text}' from: {by_locator}")
        return text
    
    def is_element_present(self, by_locator):
        # Check if an element is present
        try:
            self.fluent_wait.until(EC.presence_of_element_located(by_locator))
            self.logger.info(f"Element found: {by_locator}")
            return True
        except(TimeoutException, NoSuchElementException):
            self.logger.warning(f"Element NOT found: {by_locator}")
            return False
        
    def is_element_visible(self, by_locator):
        # Check if an element is visible
        try:
            self.fluent_wait.until(EC.visibility_of_element_located(by_locator))
            self.logger.info(f"Element visible: {by_locator}")
            return True
        except(TimeoutException, NoSuchElementException):
            self.logger.warning(f"Element NOT visible: {by_locator}")
            return False
    
    def wait_for_page_load(self):
        # Check if page is completely loaded and fully interactive
        self.explicit_wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
        self.logger.info("Page fully loaded")


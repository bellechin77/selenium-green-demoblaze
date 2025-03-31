import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from utils.constants import IMPLICIT_WAIT, EXPLICIT_WAIT, POLLING_INTERVAL

# Logging Fixture
@pytest.fixture(scope="session", autouse=True)
def logger():
    # Set up and return a logger instance as a fixture
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)  # Global log level

    # File Handler: Logs all details at DEBUG level
    file_handler = logging.FileHandler("test_logs.log")
    file_handler.setLevel(logging.DEBUG)

    # Console Handler: Logs at INFO level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger  

# WebDriver Fixture: Initializes WebDriver and Closes It After Tests
@pytest.fixture(scope="function")
def driver(logger):
    # Setup WebDriver before each test and close it after
    logger.info("Launching browser...")
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(IMPLICIT_WAIT)
        driver.maximize_window()
        yield driver
    except Exception as e:
        logger.error(f"WebDriver failed to initialize: {e}")
        raise
    finally:
        logger.info("Closing browser...")
        if 'driver' in locals():
            driver.quit()
    
# Waits Fixture: Provides Explicit Waits
@pytest.fixture
def explicit_wait(driver):
    # Returns an instance of WebDriverWait for explicit waits
    return WebDriverWait(driver, EXPLICIT_WAIT)

@pytest.fixture
def fluent_wait(driver):
    # Fixture to provide Fluent Wait with timeout and polling interval
    return WebDriverWait(driver, EXPLICIT_WAIT, poll_frequency=POLLING_INTERVAL, 
                         ignored_exceptions=[TimeoutException])

@pytest.fixture
def test_order_data():
    return {
        "name": "John Doe",
        "country": "USA",
        "city": "New York",
        "card": "4111 1111 1111 1111",
        "month": "12",
        "year": "2025"
    }
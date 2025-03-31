from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = ChromeDriverManager().install()
print(f"✅ ChromeDriver installed at: {driver_path}")

service = Service(driver_path)
driver = webdriver.Chrome(service=service)

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

# Function to add a product to the cart
def add_product(category, product_name=None, first=True, last=False):
    """Selects a category and adds a product to the cart."""
    category_element = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, f"//a[text()='{category}']"))
    )
    category_element.click()

    # Wait for products to load
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-title a"))
    )


    # Initialize product as None
    product = None

    # Select the product
    if product_name:
        product = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, product_name))
        )
    else:
        products = driver.find_elements(By.CSS_SELECTOR, ".card-title a")
        product = products[0] if first else products[-1] if last else None

    if product:
        product.click()

        # Click "Add to cart"
        add_to_cart_btn = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
        )
        add_to_cart_btn.click()

        # Handle alert
        alert = WebDriverWait(driver, 5).until(EC.alert_is_present())  
        alert.accept()

# 1️⃣ Add first phone
add_product("Phones", first=True)

# Navigate back to homepage by clicking the Home button instead of refreshing the page
home_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Home")
home_btn.click()

# 2️⃣ Add last laptop
add_product("Laptops", last=True)

# Navigate back to homepage by clicking the Home button instead of refreshing the page
home_btn = driver.find_element(By.PARTIAL_LINK_TEXT, "Home")
home_btn.click()

# 3️⃣ Add specific monitor
add_product("Monitors", product_name="Apple monitor 24")

# Navigate to the cart
cart_btn = driver.find_element(By.ID, "cartur")
cart_btn.click()

# Verify products in the cart
cart_items = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr td:nth-child(2)"))
)
cart_products = [item.text for item in cart_items]

# Ensure all 3 products are in the cart
assert "Apple monitor 24" in cart_products, "Monitor not found in cart!"
assert any("Samsung" in p or "Nokia" in p for p in cart_products), "Phone not found in cart!"
assert any("MacBook" in p or "Sony" in p for p in cart_products), "Laptop not found in cart!"
logging.info("All products are correctly added to cart ✅")

# Click on "Place Order" button
order_btn = driver.find_element(By.XPATH, "//button[text()='Place Order']")
order_btn.click()

# Wait for the order modal to appear
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.ID, "orderModal"))
)

# Fill in purchase details
driver.find_element(By.ID, "name").send_keys("John Doe")
driver.find_element(By.ID, "country").send_keys("USA")
driver.find_element(By.ID, "city").send_keys("New York")
driver.find_element(By.ID, "card").send_keys("4111 1111 1111 1111")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")

# Click "Purchase"
purchase_btn = driver.find_element(By.XPATH, "//button[text()='Purchase']")
purchase_btn.click()

# Wait for the confirmation message to appear
WebDriverWait(driver, 5).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "sweet-alert"))
)

# Verify confirmation message
confirmation_text = driver.find_element(By.CLASS_NAME, "sweet-alert").text
assert "Thank you for your purchase!" in confirmation_text, "Purchase confirmation failed!"
logging.info("Purchase confirmed ✅")

# Click OK on the confirmation popup
ok_btn = driver.find_element(By.XPATH, "//button[text()='OK']")
ok_btn.click()

# Verify redirection to homepage
assert WebDriverWait(driver, 5).until(EC.title_contains("STORE")), "❌ Redirection to homepage failed!"
logging.info("Redirected to homepage successfully ✅")

# Close browser
driver.quit()

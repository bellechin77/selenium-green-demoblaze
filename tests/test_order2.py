from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.order_page import OrderPage
from utils.config_reader import ConfigReader

def test_order(driver, fluent_wait, explicit_wait, logger, test_order_data):
    product_page = ProductPage(driver, fluent_wait, explicit_wait, logger)
    cart_page = CartPage(driver, fluent_wait, explicit_wait, logger)
    order_page = OrderPage(driver, fluent_wait, explicit_wait, logger)
    
    # Navigating to homepage
    product_page.open_url()
    
    # Add products with exception handling
    try:
        # Add first Phone product
        product_page.add_product(category="Phones", first=True)
        
        # Add last Laptop product
        product_page.add_product(category="Laptops", last=True)
        
        # Add specific Monitor product
        product_name = ConfigReader.get_property("monitor_name")
        product_page.add_product(category="Monitors", product_name=product_name)
    except Exception as e:
        logger.error(f"❌ Error adding products: {e}")
        
    # Verifying cart
    cart_page.verify_cart()

    # Placing order
    order_page.place_order(test_order_data)

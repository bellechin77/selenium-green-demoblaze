from pages.login_page import LoginPage

def test_login(driver, fluent_wait, explicit_wait, logger):
    login_page = LoginPage(driver, fluent_wait, explicit_wait, logger)
    
    # Navigating to homepage
    login_page.open_url()
        
    # Signing up a new user
    login_page.login_test_user() 
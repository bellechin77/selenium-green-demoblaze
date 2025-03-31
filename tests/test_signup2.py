from pages.signup_page import SignupPage

def test_signup(driver, fluent_wait, explicit_wait,logger):
    signup_page = SignupPage(driver, fluent_wait, explicit_wait, logger)
    
    # Navigating to homepage
    signup_page.open_url()
        
    # Signing up a new user
    signup_page.signup_new_user() 

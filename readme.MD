# Test suite: Selenium Green \- Demoblaze

## DemoBlaze Application Overview

## DemoBlaze is a simple e-commerce web application that allows users to browse, add products to a shopping cart, and complete purchases. It serves as a demo platform for testing web automation and UI interactions.

**Key Features**:  
✅ Product Catalog – Users can browse categories like Phones, Laptops, and Monitors.  
✅ Shopping Cart – Add, remove, and view selected items before checkout.  
✅ User Authentication – Signup, login, and logout functionality.  
✅ Order Placement – Users can enter their details and complete purchases.  
✅ Popup Alerts & Modals – Notifications confirm actions like adding products or completing an order.

## Enhancements

The test automation framework has been enhanced with new features, leveraging Selenium WebDriver with the Page Object Model (POM) design pattern and Pytest as the test framework.

**Key Enhancements**:

* **Page Object Model (POM):** Modular design for improved maintainability and scalability of test automation.  
* **Selenium Advanced Features:** Implementation of different types of waits, exception handling, and window interactions.  
* **Pytest Framework:** Streamlined test execution with reporting capabilities and parameterization for flexible testing.

## Automated UI Tests

The automated test strategy for **Demoblaze.com** follows a **risk-based testing approach**, prioritizing **critical functionalities** to ensure a seamless user experience. The focus is on **high-impact user journeys**, including:

✅ **Signup & Login:** Ensuring new users can register and authenticate successfully.  
 ✅ **Product Selection & Cart Management:** Validating product addition, cart persistence, and checkout readiness.  
 ✅ **End-to-End Order Placement:** Verifying smooth transactions from cart to order confirmation, ensuring critical workflows function as expected.

This approach **minimizes risks** related to broken user flows, failed transactions, and missing validation messages.

### **(1) User Story: Signup**

This story ensures that a new user can successfully create an account and receive confirmation of the action. 

| Given | When | Then |
| :---- | :---- | :---- |
| 🔹 A user is on the home page of the application. <br>🔹 The user wants to create a new account. | 🔹 The user clicks on the "Sign up" link in the navigation bar. <br>🔹 The sign-up form appears. <br>🔹 The user enters a unique username and password. <br>🔹 The user submits the sign-up form. | 🔹 The system displays an alert confirming that "Sign up successful". <br>🔹 The user remains on the home page. <br>🔹 The "Log in" button is visible in the navigation bar, indicating that the user can now log in with their his credentials. |

### **(2) User story: Login**

This user story ensures that a user can successfully log in with valid user credentials.

| Given | When | Then |
| :---- | :---- | :---- |
| 🔹 A user is on the home page of the application. <br>🔹 The user has an existing account with a valid username and password. <br>🔹 The "Log in" button is visible in the navigation menu. | 🔹 The user clicks on the "Log in" button. <br>🔹 The login modal appears. <br>🔹 The user enters valid credentials. <br>🔹 The user clicks the "Log in" button in the modal. | 🔹 The login modal closes. <br>🔹 A welcome message appears in the navigation bar, displaying "Welcome \[username\]".  |

### **(3) User story: Order**

This user story outlines the key steps involved in adding products to the cart, confirming the order, and verifying the purchase success message.

| Given | When | Then |
| :---- | :---- | :---- |
| 🔹 A user is on the home page of the application. <br>🔹 The category menu is visible, allowing the user to browse product categories. | 🔹 The user selects the Phones category and adds the first available phone to the cart. <br>🔹 The user selects the Laptops category and adds the last available laptop to the cart. <br>🔹 The user selects the Monitors category and adds a specific product, "Apple monitor 24," to the cart. <br>🔹 The user navigates to the Cart page and verifies that all three selected products are present. <br>🔹 The user proceeds to Place an Order, fills in the required details (Name, Country, City, Credit Card, Month, Year), and clicks on Purchase. | 🔹 A confirmation popup appears with the message "Thank you for your purchase\!" <br>🔹 The user clicks OK on the confirmation popup. <br>🔹 The user is redirected back to the homepage, completing the purchase process.  |

### 

### Test Cases added

| User story | Test case |
| :---- | :---- |
| Signup  | test\_signup2.py |
| Login  | test\_login2.py |
| Order | test\_order2.py |

## **📁 Project Structure**

```
selenium_project/
│── pages/
│   ├── base_page.py       # Parent class for page objects
│   ├── signup_page.py     # Signup page automation
│   ├── login_page.py      # Login page automation
│   ├── product_page.py    # Product selection automation
│   ├── cart_page.py       # Cart verification automation
│   ├── order_page.py      # Order placement automation
│
│── tests/
│   ├── test_signup2.py     # Signup test
│   ├── test_login2.py      # Login test
│   ├── test_order2.py      # Order placement test
│
│── utils/
│   ├── config_reader.py    # Utility for reading config.properties
│   ├── constants.py   	    # Constant values
│
│── conftest.py            # Pytest configuration and fixtures
│── config.properties      # Configuration properties
│── readme.MD              # Documentation
```

---

## Acceptance criteria

### (1) Usage of Page Object Models 

The framework is designed using the **Page Object Model (POM)** for better maintainability and scalability.

#### 🔹 Class: BasePage

| Description | Parent class for all other page objects, encapsulating reusable methods for interacting with web elements |
| :---- | :---- |
| **Purpose** | Provides common utility functions like click, enter\_text, get\_text, and various element checks, reduces code duplication across individual page objects, ensures consistency in the way elements are interacted with,  and improves maintainability in test suites. |
| **Methods** |  |
| **Constructor (`__init__`)**: | 🔹 Initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 These attributes are then available to all subclasses that inherit from `BasePage`. |
| **open\_url()**: | 🔹 Opens the base URL (configured via `ConfigReader`) in the browser. <br>🔹 Logs the action to indicate which URL is being opened. |
| **click()**: | 🔹 Waits for an element to be clickable and then performs a click action. <br>🔹 Logs the element being clicked for traceability. |
| **enter\_text()**: | 🔹 Clears and enters text into a specified input field. <br>🔹 Logs the text being entered and the field being targeted. |
| **get\_text()**: | 🔹 Waits for an element to become visible, retrieves its text content, and returns it. <br>🔹 Logs the text retrieved for debug purposes. |
| **is\_element\_present()**: | 🔹 Checks if an element is present in the DOM using a presence check. <br>🔹 Returns `True` if the element is found, and `False` otherwise. <br>🔹 Logs the presence or absence of the element. |
| **is\_element\_visible()**: | 🔹 Waits for an element to become visible (not just present in the DOM). <br>🔹 Returns `True` if the element is visible, and `False` otherwise. <br>🔹 Logs the visibility status of the element. |

#### 🔹 Class: SignupPage

| Description | Page object model representing the signup page of a web application, it contains methods for interacting with elements on the signup page and performing the necessary steps for signing up a new user. |
| :---- | :---- |
| **Purpose** | Provides methods for interacting with the signup page, entering user credentials, submitting the signup form, and handling the success message |
| **Methods** |  |
| **Constructor(`__init__`)**: | 🔹 Inherits from the `BasePage` class and initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 Defines locators for key elements on the signup page, such as the signup button, modal, input fields, and confirmation button. |
| **signup\_new\_user()**: | 🔹 Orchestrates the signup process by calling the relevant methods to open the signup modal, enter user credentials, submit the form, and handle the success alert. <br>🔹 Catches any exceptions (e.g., `TimeoutException`, `NoSuchElementException`) that may occur during the signup process and logs an appropriate error message. |
| **open\_signup\_modal()**: | 🔹 Clicks the "Signup" button to open the signup modal. <br>🔹 Verifies that the modal appears within a reasonable amount of time. <br>🔹 Logs the steps of opening the modal and raises an error if the modal doesn't appear. |
| **enter\_credentials()**: | 🔹 Generates random credentials (username and password) by appending a unique string (UUID) to predefined values from the configuration. <br>🔹 Enters the generated username and password into the corresponding fields in the signup form. <br>🔹 Logs the action and raises an error if the fields are not interactable. |
| **submit\_signup()**: | 🔹 Clicks the "Sign Up" button to submit the signup form. <br>🔹 Waits for an alert to appear as confirmation of the signup process. <br>🔹 Logs the submission action and raises an error if no alert appears. |
| **handle\_alert()**: | 🔹 Handles the alert that appears after the signup form is submitted. <br>🔹 Verifies that the alert contains a message confirming successful signup ("Sign up successful"). <br>🔹 Accepts the alert and logs the success, or raises an assertion error if the alert message is unexpected. <br>🔹 Handles unexpected alerts by logging the issue. |

#### 🔹 Class: LoginPage

| Description | Page object model that represents the login page of a web application, it contains methods to interact with the login page, perform user login actions, and verify successful login. |
| :---- | :---- |
| **Purpose** | Provides methods for opening the login modal, entering credentials, submitting the login form, and checking the welcome text that confirms successful login |
| **Methods** |  |
| **Constructor (`__init__`):** | 🔹 Inherits from the `BasePage` class and initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 Defines locators for key elements on the login page, such as the login button, modal, input fields, login confirmation button, and the welcome text. |
| **login\_test\_user():** | 🔹 Orchestrates the login process by calling the relevant methods to open the login modal, enter credentials, submit the login form, and verify the welcome text. <br>🔹 Catches exceptions such as `TimeoutException` and `NoSuchElementException` during the login process, logging appropriate error messages when an issue arises. |
| **open\_login\_modal():** | 🔹 Clicks the "Login" button to open the login modal. <br>🔹 Verifies that the modal appears within a reasonable amount of time. <br>🔹 Logs the process of opening the modal and raises an error if the modal is not visible. |
| **enter\_credentials():** | 🔹 Retrieves the test username and password from the configuration and appends a unique test ID (`TEST_USER_ID`) for testing purpose. <br>🔹 Logs the action of entering credentials but hides the password from being shown. <br>🔹 Fills in the username and password fields in the login form. <br>🔹 Raises an error if the fields are not interactable. |
| **submit\_login():** | 🔹 Clicks the "Log in" button to submit the login form. <br>🔹 Logs the action and raises an error if the button is not clickable, using exceptions like `NoSuchElementException`, `TimeoutException`, or `StaleElementReferenceException`. |
| **get\_welcome\_text():** | 🔹 Retrieves the welcome text after logging in, confirming that the user has been successfully authenticated. <br>🔹 Logs the retrieved welcome text and raises an error if the text cannot be retrieved due to exceptions such as `NoSuchElementException` or `TimeoutException`. |
| **verify\_welcome\_text():** | 🔹 Asserts that the welcome text contains the expected text, which includes the test username. <br>🔹 If the expected text is not found, raises an assertion error and logs the failure. |

#### 🔹 Class: ProductPage

| Description | Page object model that represents the product page of the application, it includes methods for interacting with the product list, selecting a product from a category, adding it to the cart, and navigating back to the homepage. |
| :---- | :---- |
| **Purpose** | Handles all interactions related to the product page, such as selecting a product from a category, adding it to the cart, and navigating back to the homepage |
| **Methods** |  |
| **Constructor (`__init__`):** | 🔹 Inherits from the `BasePage` class and initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 Defines locators for key elements such as category links, product links, add to cart button, and the home button. |
| **add\_product():** | **Parameters**: <br>`category`: The category to select a product from. <br>`product_name`: Optional parameter to specify the exact product name. <br>`first`: Boolean flag to choose the first product in the list (defaults to `False`). <br>`last`: Boolean flag to choose the last product in the list (defaults to `False`). <br> **Description**: <br>🔹 Selects a product from a given category and adds it to the cart. <br>🔹 Clicks on the specified category, waits for the products to appear, and selects either the first, last, or specified product. <br>🔹 After selecting the product, clicks the "Add to Cart" button and accepts the alert pop-up confirming the product has been added to the cart. <br>🔹 Finally, navigates back to the homepage. <br> **Exception Handling**: <br>🔹 Raises `TimeoutException` or `NoSuchElementException` if the category or product cannot be found. |
| **add\_to\_cart\_and\_accept():** | **Description**: <br>🔹 Clicks the "Add to Cart" button for the selected product and waits for an alert to confirm the product has been added. <br>🔹 The alert is accepted, confirming the action was successful. <br>**Exception Handling**: <br>🔹 Handles `TimeoutException` if the alert is not found, and `ElementClickInterceptedException` if the "Add to Cart" button is blocked by another element. |
| **navigate\_to\_home():** | **Description**: <br>🔹 Navigates back to the homepage after adding the product to the cart. <br>🔹 It clicks the "Home" button and waits for the homepage elements (e.g., carousel) to load, confirming that the navigation was successful. <br>**Exception Handling**: <br>🔹 Raises `TimeoutException` if the homepage does not load correctly or if the "Home" button is not clickable. |

#### 🔹 Class: CartPage

| Description | Page object model that represents the shopping cart page of the application, it provides methods for verifying the cart's contents, navigating to the cart, and retrieving the products in the cart. |
| :---- | :---- |
| **Purpose** | Manages interactions with the shopping cart page. It allows tests to verify the contents of the cart, navigate to the cart page, and handle issues like timeouts, stale elements, and retries.  |
| **Methods** |  |
| **Constructor (`__init__`):** | 🔹 Inherits from the `BasePage` class and initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 Defines locators for key elements such as the cart button and cart items in the cart list. |
| **verify\_cart():** | **Parameters**: <br>`max_retries`: Maximum number of retry attempts (default: 3). <br>`delay`: Delay between retries (default: 2 seconds). <br>**Description**: <br>🔹 Verifies that the cart contains specific products (Samsung, Nokia, MacBook, Sony, Apple monitor 24). <br>🔹 Uses the `get_cart_products_with_retry` method to handle retries in case products are not available initially. <br>🔹 Raises assertion errors if any expected product is missing from the cart. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException`, `AssertionError`, and `WebDriverException` to handle various error scenarios and logs the appropriate error messages. |
| **navigate\_to\_cart():** | **Description**: <br>🔹 Clicks on the cart button to navigate to the cart page. <br>🔹 Refreshes the page to ensure all items are loaded correctly. <br>🔹 Waits for the cart items to appear, ensuring the cart page is fully loaded. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException` and `NoSuchElementException` to handle cases where the cart page or the cart button cannot be found. |
| **get\_cart\_products():** | **Description**: <br>🔹 Retrieves the list of product names from the cart. <br>🔹 Waits for multiple cart items to appear before proceeding, ensuring the cart is populated with products. <br>🔹 Handles stale elements by retrying if necessary. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException`, `NoSuchElementException`, and `StaleElementReferenceException` to handle issues like slow loading or stale elements, retrying the process as needed. |
| **get\_cart\_products\_with\_retry():** | **Description**: <br>🔹 Retries getting the cart products with a maximum number of retries. <br>🔹 Waits dynamically for new elements to appear in the cart. <br>**Exception Handling**: <br>🔹 Catches `StaleElementReferenceException` and `TimeoutException`, retrying up to the specified number of attempts if elements are stale or the cart takes too long to load. |

#### 🔹 Class: OrderPage

| Description | Page object model that represents the order confirmation page in the application. It provides methods for placing an order, filling out order details, submitting the order, verifying the confirmation message, and handling the confirmation popup |
| :---- | :---- |
| **Purpose** | Handles the interactions necessary for placing an order in the application. It provides functionality to open the order modal, fill in the required order details, submit the order, and verify that the purchase was successful through confirmation messages and popups.  |
| **Methods** |  |
| **Constructor (`__init__`):** | 🔹 Inherits from the `BasePage` class and initializes the WebDriver (`driver`), Fluent Wait (`fluent_wait`), Explicit Wait (`explicit_wait`) and Logger (`logger`). <br>🔹 Defines locators for the "Place Order" button, order modal, form fields (name, country, city, card, month, year), the "Purchase" button, confirmation text, and the "OK" button in the confirmation popup. |
| **place\_order():** | **Parameters**: <br>`order_data`: A dictionary containing order details (e.g., name, country, city, card number, month, and year). <br>**Description**: <br>🔹 Orchestrates the order placement by opening the order modal, filling in order details, submitting the order, and verifying the order confirmation. <br>🔹 Confirms the purchase via the confirmation popup after successful order placement. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException`, `NoSuchElementException`, and `WebDriverException` to handle errors such as timeouts, missing elements, or WebDriver-related issues during the order process. |
| **open\_order\_modal():** | **Description**: <br>🔹 Opens the order modal by clicking the "Place Order" button. <br>🔹 Waits for the modal to become visible before proceeding. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException` in case the modal fails to open within the expected time. |
| **fill\_order\_details():** | **Parameters**: <br>`order_data`: A dictionary containing the order details to be entered in the form fields. <br>**Description**: <br>🔹 Fills in the order form with provided data by iterating through the `order_data` dictionary and populating the corresponding fields (e.g., name, country, city, card details). <br>🔹 Logs warnings for any unexpected fields in the provided test data. <br>**Exception Handling**: <br>🔹 Catches `NoSuchElementException` if any of the form fields are not found. |
| **submit\_order():** | **Description**:** <br>🔹 Submits the order by clicking the "Purchase" button. <br>🔹 Logs the submission status for verification. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException` if the "Purchase" button cannot be clicked within the expected time. |
| **verify\_confirmation():** | **Description**: <br>🔹 Verifies that the order confirmation message appears after the order is submitted. <br>🔹 Checks whether the confirmation message contains the text "Thank you for your purchase\!". <br>**Exception Handling**: <br>Catches `NoSuchElementException` if the confirmation message is not found. |
| **confirm\_popup():** | **Description**: <br>🔹 Confirms the order by clicking the "OK" button in the confirmation popup. <br>**Exception Handling**: <br>🔹 Catches `TimeoutException` if the "OK" button cannot be clicked within the expected time. |

### (2) Local Test Environment Setup

A **local test environment** is set up for automating tests on the **Demoblaze.com** application. This setup incorporates **Python**, a **virtual environment**, and the **Selenium WebDriver** with the **Pytest** framework.

All dependencies, including **Selenium, Pytest, and WebDriver Manager**, are installed within the virtual environment to ensure isolation and consistency across test executions. The WebDriver Manager simplifies browser driver handling, eliminating manual downloads. 

With **Pytest**, test execution is more efficient, supporting parameterization and detailed reporting. Now, running the test suite is as simple as executing `pytest`, making it easier to validate application functionality.

#### Step-by-Step Guide

#### **1\. Install Python**

* Download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)  
* Run the installer and **check the box** for **"Add Python to PATH"** before proceeding with the installation.  
* Verify the installation by running `python --version` (Windows) or `python3 --version` (Mac/Linux) in the terminal or command prompt.

#### **2\. Set Up a Virtual Environment**

* Open a terminal or command prompt and navigate to the desired project directory.  
* Create a virtual environment:  
  * **Windows**: `python -m venv venv`  
  * **Mac/Linux**: `python3 -m venv venv`  
* Activate the virtual environment:  
  * **Windows**: `venv\Scripts\activate`  
  * **Mac/Linux**: `source venv/bin/activate`

#### **3\. Install Selenium and Pytest**

Install Selenium, Pytest, and WebDriver Manager using:  
`pip install selenium pytest webdriver-manager`

#### **4\. Set Up WebDriver for Browser Automation**

* Selenium requires a browser driver (e.g., ChromeDriver for Chrome). Instead of downloading it manually, use `webdriver-manager` to manage it automatically within your test scripts.

#### **5\. Write and Organize Tests with Pytest**

* Create a **`tests`** directory inside your project folder.  
* Write the test file, such as `test_signup2.py`, inside the `tests` directory.

#### **6\. Run Tests Using Pytest**

Execute tests by running: `pytest`  
For a detailed report, install Pytest HTML reporting: `pip install pytest-html`  
Generate an HTML report: `pytest --html=report.html`

This setup ensures a modular and maintainable test automation framework using Selenium and Pytest. 

### (3) Fixtures implemented with the Pytest Framework

These fixtures are integrated to enhance **test modularity, maintainability, and reliability** by providing reusable setups for logging, WebDriver management, and synchronization strategies

| Fixture | Scope | Purpose |
| ----- | ----- | ----- |
| **`logger`** | `session` | Sets up a logging mechanism with file and console handlers to track test execution details. |
| **`driver`** | `function` | Initializes and provides a Selenium WebDriver instance before each test, applies implicit wait, maximizes the window, and ensures proper cleanup after test execution |
| **`explicit_wait`** | `function` | Provides an instance of `WebDriverWait` for explicit waits, ensuring synchronization before interacting with elements |
| **`fluent_wait`** | `function` | Sets up Fluent Wait with polling intervals and exception handling for dynamic element interactions |
| **`test_order_data`** | `function` | Supplies predefined test data for order placement, including user details and payment information |

### (4) Usage of Waits

Different types of **waits** are used in the test automation framework to improve test stability and reliability.

| Wait Type | Used In | Purpose |
| ----- | ----- | ----- |
| **Implicit Wait** | `BasePage.__init__` | Sets a default wait time for all elements before throwing `NoSuchElementException` |
| **Explicit Wait** | `BasePage.click` | Waits for an element to be clickable before performing a click action |
|  | `SignupPage.submit_signup` | Waits for an alert to be present after signup |
|  | `SignupPage.handle_alert` | Waits for the signup confirmation alert before interacting |
|  | `CartPage.verify_cart` | Ensures cart contents are verified within a set timeout |
|  | `CartPage.navigate_to_cart` | Waits for the cart page elements to load fully |
|  | `OrderPage.open_order_modal` | Waits for the order modal to be visible after clicking 'Place Order’ |
| **Fluent Wait** | `BasePage.is_element_present` | Checks for the presence of an element with retries |
|  | `BasePage.is_element_visible` | Ensures an element is visible with retries |
|  | `ProductPage.add_product` | Waits for product elements to load dynamically |
|  | `ProductPage.navigate_to_home` | Waits for the homepage carousel to be fully loaded after navigation |
|  | `CartPage.get_cart_products` | Waits for multiple cart items to be visible before fetching them |
|  | `CartPage.get_cart_products_with_retry` | Retries fetching cart items if stale elements are encountered |

### (3) Window Interactions

The automated tests involve various **window interactions** to simulate a real user journey. The key interactions across different pages include:

| Interaction Type | Test Page & Method | Description |
| ----- | ----- | ----- |
| **Alert Handling**  | `SignupPage.handle_alert()` | Waits for the signup confirmation alert, retrieves its text, and accepts it. |
|  | `ProductPage.add_to_cart_and_accept()` | Waits for the "Add to Cart" confirmation alert and accepts it. |
| **Popup Handling** | `OrderPage.confirm_popup()` | Waits for the order confirmation popup and clicks the "OK" button. |
| **Modal Window Handling**  | `SignupPage.open_signup_modal()` | Clicks "Sign Up" and waits for the signup modal to appear |
|  | `OrderPage.open_order_modal()` | Clicks "Place Order" and waits for the order modal to be visible |
| **Window Refresh** | `CartPage.navigate_to_cart()` | Clicks the cart button and refreshes the page to ensure all items are loaded |

### (5) Exception Handlings

These exceptions are handled in the automated tests to ensure **robust error handling** during test execution, allowing tests to recover or fail while logging useful debugging information.

| Exception | Test Page & Method | Handling Approach |
| ----- | ----- | ----- |
| **`TimeoutException`** | `SignupPage.handle_alert()`, `ProductPage.add_to_cart_and_accept()`, `CartPage.verify_cart()`, `OrderPage.place_order()` | Logs an error message and raises the exception when an expected element or alert does not appear within the wait time |
| **`NoSuchElementException`** | `SignupPage.signup_new_user()`, `CartPage.get_cart_products()`, `OrderPage.fill_order_details()` | Logs an error and raises the exception if an expected element is not found |
| **`ElementClickInterceptedException`** | `ProductPage.add_to_cart_and_accept()` | Logs an error and raises the exception when an element is blocked from being clicked |
| **`StaleElementReferenceException`** | `CartPage.get_cart_products()`, `CartPage.get_cart_products_with_retry()` | Retries locating the element if it becomes stale (e.g. no longer attached to the DOM) |
| **`UnexpectedAlertPresentException`** | `SignupPage.handle_alert()` | Logs an error and raises the exception if an unexpected alert appears |
| **`WebDriverException`** | `CartPage.verify_cart()`, `OrderPage.place_order()` | Handles general WebDriver issues and logs an error before raising the exception |
| **`AssertionError`** | `SignupPage.handle_alert()`, `CartPage.verify_cart()` | Raised when verification of expected results fails (e.g., incorrect cart contents or unexpected alert messages) |


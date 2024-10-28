# Automation Testing Script - Selenium Python

## Project Overview
This project automates a checkout process on the [Automation Exercise](https://automationexercise.com/) e-commerce site. Using Selenium with Python, it verifies that the critical flow for adding a product to the cart and completing a checkout process works as expected. The test scripts are organized using the Page Object Model (POM) to ensure code reusability and maintainability.

## Table of Contents
- [Project Overview](#project-overview)
- [Test Scenario](#test-scenario)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Tests](#running-the-tests)
- [Generating Test Reports with Allure](#generating-test-reports-with-allure)
- [Technologies Used](#technologies-used)

## Test Scenario
1. Navigate to the [Automation Exercise](https://automationexercise.com/) website.
2. Select a product and add it to the cart.
3. Click "View Cart" on the overlay to proceed to the cart page.
4. On the cart page, click "Proceed To Checkout."
5. On the checkout page, enter the billing information, including:
   - Name on card
   - Card number
   - CVC
   - Expiration date (MM YYYY)
6. Click "Pay and Confirm Order."
7. Verify that the order is successfully placed and displays the confirmation message.

## Project Structure
The project follows a structured approach using the Page Object Model (POM) pattern:

Automation-Testing-Script-Selenium-Paython/ ├── pages/ # Contains page classes │ ├── base_page.py # BasePage class for common functionality │ ├── product_page.py # ProductPage class for product selection and adding to cart │ ├── cart_page.py # CartPage class for cart actions │ ├── checkout_page.py # CheckoutPage class for checkout actions │ └── order_confirmation_page.py # OrderConfirmationPage class to verify order placement ├── tests/ # Contains test cases │ └── test_checkout.py # Test case for the checkout flow ├── README.md # Project documentation 


## Setup Instructions

### Prerequisites
- **Python** (3.7+)
- **Google Chrome** and **ChromeDriver** matching your Chrome version.
- **Git** (if cloning from GitHub)

### Install Dependencies
1. Clone the repository:

   ```bash
   git clone https://github.com/amrgamalhan/Automation-Testing-Script-Selenium-Paython.git
   cd Automation-Testing-Script-Selenium-Paython

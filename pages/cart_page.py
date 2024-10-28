# cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.proceed_to_checkout_button = (By.XPATH, "//button[contains(text(), 'Proceed to checkout')]")

    def proceed_to_checkout(self):
        self.driver.find_element(*self.proceed_to_checkout_button).click()
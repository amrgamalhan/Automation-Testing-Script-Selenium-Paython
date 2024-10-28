# product_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.XPATH, "//button[contains(text(), 'Add to cart')]")

    def add_product_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

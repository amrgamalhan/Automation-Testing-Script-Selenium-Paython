# pages/order_confirmation_page.py
from selenium.webdriver.common.by import By

class OrderConfirmationPage:
    def __init__(self, driver):
        self.driver = driver
        self.confirmation_message = (By.XPATH, "//h2[contains(text(), 'Order Placed!')]")

    def is_order_confirmed(self):
        return "Order Placed!" in self.driver.page_source

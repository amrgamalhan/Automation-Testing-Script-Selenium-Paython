# pages/billing_page.py
from selenium.webdriver.common.by import By

class BillingPage:
    def __init__(self, driver):
        self.driver = driver
        self.card_name_field = (By.NAME, "card_name")
        self.card_number_field = (By.NAME, "card_number")
        self.cvc_field = (By.NAME, "cvc")
        self.expiration_field = (By.NAME, "expiration")
        self.pay_button = (By.XPATH, "//button[contains(text(), 'Pay and Confirm Order')]")

    def enter_payment_info(self, card_name, card_number, cvc, expiration):
        self.driver.find_element(*self.card_name_field).send_keys(card_name)
        self.driver.find_element(*self.card_number_field).send_keys(card_number)
        self.driver.find_element(*self.cvc_field).send_keys(cvc)
        self.driver.find_element(*self.expiration_field).send_keys(expiration)

    def confirm_payment(self):
        self.driver.find_element(*self.pay_button).click()

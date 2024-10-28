# pages/checkout_page.py
from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = (By.NAME, "name")
        self.address_field = (By.NAME, "address")
        self.city_field = (By.NAME, "city")
        self.state_field = (By.NAME, "state")
        self.zip_code_field = (By.NAME, "zipcode")
        self.place_order_button = (By.XPATH, "//button[contains(text(), 'Place Order')]")

    def enter_shipping_info(self, name, address, city, state, zipcode):
        self.driver.find_element(*self.name_field).send_keys(name)
        self.driver.find_element(*self.address_field).send_keys(address)
        self.driver.find_element(*self.city_field).send_keys(city)
        self.driver.find_element(*self.state_field).send_keys(state)
        self.driver.find_element(*self.zip_code_field).send_keys(zipcode)

    def place_order(self):
        self.driver.find_element(*self.place_order_button).click()

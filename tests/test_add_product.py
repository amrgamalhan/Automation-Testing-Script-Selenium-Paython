import time
from selenium import webdriver
from pages.product_page import ProductPage

def test_add_product_to_cart():
    driver = webdriver.Chrome()
    product_page = ProductPage(driver)

    product_page.open_url("https://automationexercise.com")
    product_page.add_product_to_cart()
    
    time.sleep(5)  # Delay to observe the browser before it closes

    driver.quit()
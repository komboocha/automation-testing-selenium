from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ShopProductPage:
    def __init__(self, browser):
        self.browser = browser

    def size_option(self, size):
        size_option = Select(self.browser.find_element(By.CSS_SELECTOR, "[data-product-attribute='1']"))
        size_option.select_by_visible_text(size)

    def increase_quantity(self):
        increase_quantity = self.browser.find_element(By.CSS_SELECTOR, ".touchspin-up")
        increase_quantity.click()

    def decrease_quantity(self):
        quantity_decrease = self.browser.find_element(By.CSS_SELECTOR, ".touchspin-down")
        quantity_decrease.click()

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(By.CSS_SELECTOR, ".add-to-cart.btn.btn-primary")
        add_to_cart.click()

    def go_back_to_homepage(self):
        home_page = self.browser.find_element(By.XPATH, "//span[.='Home']")
        home_page.click()


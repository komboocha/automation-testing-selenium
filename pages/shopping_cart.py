from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ShoppingCart:
    def __init__(self, browser):
        self.browser = browser

    def have_promo_code(self):
        promo_code = self.browser.find_element(By.LINK_TEXT, "Have a promo code?")
        promo_code.click()

    def enter_promo_code(self, promo_code):
        promo_text_box = self.browser.find_element(By.CSS_SELECTOR, "input[name = 'discount_name']")
        promo_text_box.send_keys(promo_code)

    def proceed_to_checkout(self):
        proceed_to_checkout = self.browser.find_element(By.LINK_TEXT, "PROCEED TO CHECKOUT")
        proceed_to_checkout.click()

    def delete_item_one(self):
        item_one = self.browser.find_element(By.CSS_SELECTOR, ".cart-items .cart-item:nth-of-type(1) .float-xs-left")
        item_one.click()

    def delete_item_two(self):
        item_two = self.browser.find_element(By.CSS_SELECTOR, ".cart-items .cart-item:nth-of-type(2) .float-xs-left")
        item_two.click()

    def wait_for_item_deleted(self, item):
        wait = WebDriverWait(self.browser, 10)
        item = (By.CSS_SELECTOR, item)
        wait.until(expected_conditions.invisibility_of_element(item))

    def total_value(self):
        total_value = self.browser.find_element(By.CSS_SELECTOR, ".cart-total .value")
        return total_value.text

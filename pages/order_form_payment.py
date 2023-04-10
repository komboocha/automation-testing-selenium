from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class OrderFormPayment:
    def __init__(self, browser):
        self.browser = browser

    def pay_by_check(self):
        pay_by_check = self.browser.find_element(By.XPATH, "//span[.='Pay by Check']")
        pay_by_check.click()

    def pay_by_wire(self):
        pay_by_wire = self.browser.find_element(By.XPATH, "//span[.='Pay by bank wire']")
        pay_by_wire.click()

    def agree_to_terms_and_conditions(self):
        check_box = self.browser.find_element(By.XPATH, "//input[@id='conditions_to_approve[terms-and-conditions]']")
        check_box.click()

    def wait_for_order_button_to_load(self):
        wait = WebDriverWait(self.browser, 10)
        button = self.browser.find_element(By.XPATH, "//div[@id='payment-confirmation']//button[@type='submit']")
        wait.until(expected_conditions.element_to_be_clickable(button))

    def click_order_button(self):
        button = self.browser.find_element(By.XPATH, "//div[@id='payment-confirmation']//button[@type='submit']")
        button.click()


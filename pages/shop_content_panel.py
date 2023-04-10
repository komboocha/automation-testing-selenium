from selenium.webdriver.common.by import By


class ShopContentPanel:
    def __init__(self, browser):
        self.browser = browser

    def continue_shopping_button(self):
        continue_shopping_button = self.browser.find_element(By.XPATH, "//button[contains(text(),'Continue')]")
        continue_shopping_button.click()

    def proceed_to_checkout(self):
        checkout_button = self.browser.find_element(By.CSS_SELECTOR, ".cart-content-btn .btn-primary")
        checkout_button.click()


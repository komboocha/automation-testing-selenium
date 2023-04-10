from selenium.webdriver.common.by import By


class OrderFormShipping:
    def __init__(self, browser):
        self.browser = browser

    def enter_comment(self, comment):
        comment_text_box = self.browser.find_element(By.CSS_SELECTOR, "textarea#delivery_message")
        comment_text_box.send_keys(comment)

    def click_continue_button(self):
        continue_button = self.browser.find_element(By.CSS_SELECTOR, "[name='confirmDeliveryOption']")
        continue_button.click()


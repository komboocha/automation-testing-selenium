from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, browser):
        self.browser = browser

    def toggle_button_click(self):
        toggle_button = self.browser.find_element(By.CSS_SELECTOR, ".toggle")
        toggle_button.click()

    def homepage(self):
        homepage = self.browser.find_element(By.LINK_TEXT, "HOMEPAGE")
        return homepage

    def accordion_link_click(self):
        accordion = self.browser.find_element(By.LINK_TEXT, "ACCORDION")
        accordion.click()

    def click_store_link(self):
        store_link = self.browser.find_element(By.LINK_TEXT, "TEST STORE")
        store_link.click()

    def close_cookie_warning(self):
        cookie_warning = self.browser.find_element(By.CSS_SELECTOR, ".close-cookie-warning span")
        cookie_warning.click()

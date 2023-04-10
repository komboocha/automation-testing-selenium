from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class OrderFormDelivery:
    def __init__(self, browser):
        self.browser = browser

    def enter_address(self, address):
        address_field = self.browser.find_element(By.CSS_SELECTOR, "input[name='address1']")
        address_field.send_keys(address)

    def enter_city(self, city):
        city_field = self.browser.find_element(By.CSS_SELECTOR, "input[name='city']")
        city_field.send_keys(city)

    def select_state(self, state):
        state_dropdown = Select(self.browser.find_element(By.CSS_SELECTOR, "select[name='id_state']"))
        state_dropdown.select_by_visible_text(state)

    def enter_postal_code(self, postal_code):
        postal_code_field = self.browser.find_element(By.CSS_SELECTOR, "input[name='postcode']")
        postal_code_field.send_keys(postal_code)

    def select_country(self, country):
        country_dropdown = Select(self.browser.find_element(By.CSS_SELECTOR, "select[name='id_country']"))
        country_dropdown.select_by_visible_text(country)

    def click_continue_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "button[name='confirm-addresses']")
        button.click()

from selenium.webdriver.common.by import By


class OrderForm:
    def __init__(self, browser):
        self.browser = browser

    def select_gender_mr(self):
        gender_mr = self.browser.find_element(By.CSS_SELECTOR,
                                              "label:nth-of-type(1) > .custom-radio > input[name='id_gender']")
        gender_mr.click()

    def select_gender_ms(self):
        gender_ms = self.browser.find_element(By.CSS_SELECTOR,
                                              "label:nth-of-type(2) > .custom-radio > input[name='id_gender']")
        gender_ms.click()

    def enter_first_name(self, name):
        first_name = self.browser.find_element(By.CSS_SELECTOR, "input[name='firstname']")
        first_name.send_keys(name)

    def enter_last_name(self, last_name):
        first_name = self.browser.find_element(By.CSS_SELECTOR, "input[name='lastname']")
        first_name.send_keys(last_name)

    def enter_email(self, email):
        email_field = self.browser.find_element(By.CSS_SELECTOR, "form#customer-form > section input[name='email']")
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.browser.find_element(By.CSS_SELECTOR,
                                                   "form#customer-form > section input[name='password']")
        password_field.send_keys(password)

    def enter_birthdate(self, birthdate):
        birthdate_field = self.browser.find_element(By.CSS_SELECTOR, "input[name='birthday']")
        birthdate_field.send_keys(birthdate)

    def receive_partner_offers(self):
        checkbox = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(7)  span > label > span")
        checkbox.click()

    def sign_up_for_newsletter(self):
        checkbox = self.browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(8)  span > label > span")
        checkbox.click()

    def agree_to_terms_and_conditions(self):
        checkbox = self.browser.find_element(By.CSS_SELECTOR, "input[name='psgdpr']")
        checkbox.click()

    def click_continue_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "form#customer-form  button[name='continue']")
        button.click()

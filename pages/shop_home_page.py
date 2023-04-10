from selenium.webdriver.common.by import By


class ShopHomePage:
    def __init__(self, browser):
        self.browser = browser

    def select_product_one(self):
        product_one = self.browser.find_element(By.LINK_TEXT, "Hummingbird Printed T-Shirt")
        product_one.click()

    def select_product_two(self):
        product_two = self.browser.find_element(By.LINK_TEXT, "Hummingbird Printed Sweater")
        product_two.click()

    def select_product_three(self):
        product_three = self.browser.find_element(By.LINK_TEXT, "The Best Is Yet To Come'...")
        product_three.click()

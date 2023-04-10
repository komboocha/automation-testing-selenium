from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Edge
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


def test_chrome_selenium_test():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.automationtesting.co.uk/')

    browser.maximize_window()
    time.sleep(3)
    browser.quit()


def test_firefox_selenium_test():
    browser = Firefox(executable_path=GeckoDriverManager().install())
    browser.get('https://www.automationtesting.co.uk/')

    browser.maximize_window()
    time.sleep(3)
    browser.quit()


def test_edge_selenium_test():
    browser = Edge(executable_path=EdgeChromiumDriverManager().install())
    browser.get('https://www.automationtesting.co.uk/')

    browser.maximize_window()
    time.sleep(3)
    browser.quit()

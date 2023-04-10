import time
import pytest
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.shop_home_page import ShopHomePage
from pages.shop_product_page import ShopProductPage
from pages.shop_content_panel import ShopContentPanel
from pages.shopping_cart import ShoppingCart


@pytest.fixture
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.automationtesting.co.uk/')
    browser.maximize_window()
    yield browser
    browser.quit()


def test_add_remove_item(browser):
    home = HomePage(browser)
    home.close_cookie_warning()
    home.click_store_link()

    shop_home = ShopHomePage(browser)
    shop_home.select_product_one()

    shop_product = ShopProductPage(browser)
    shop_product.size_option('M')
    shop_product.increase_quantity()
    shop_product.add_to_cart()
    time.sleep(2)
    shop_content_panel = ShopContentPanel(browser)
    shop_content_panel.continue_shopping_button()

    shop_product.go_back_to_homepage()
    shop_home.select_product_two()
    shop_product.add_to_cart()
    time.sleep(2)
    shop_content_panel.proceed_to_checkout()
    shopping_cart = ShoppingCart(browser)
    shopping_cart.delete_item_two()
    shopping_cart.wait_for_item_deleted(".cart-items .cart-item:nth-of-type(2) .float-xs-left")

    assert shopping_cart.total_value() == '$45.24'





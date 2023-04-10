import pytest
import time
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from pages.home_page import HomePage
from pages.shop_home_page import ShopHomePage
from pages.shop_product_page import ShopProductPage
from pages.shop_content_panel import ShopContentPanel
from pages.shopping_cart import ShoppingCart
from pages.order_form_info import OrderForm
from pages.order_form_delivery import OrderFormDelivery
from pages.order_form_shipping import OrderFormShipping
from pages.order_form_payment import OrderFormPayment


@pytest.fixture
def browser():
    browser = Chrome(executable_path=ChromeDriverManager().install())
    browser.get('https://www.automationtesting.co.uk/')
    browser.maximize_window()
    yield browser
    browser.quit()


def test_end_to_end_test(browser):
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
    shop_content_panel.proceed_to_checkout()

    shopping_cart = ShoppingCart(browser)
    shopping_cart.have_promo_code()
    shopping_cart.enter_promo_code('20OFF')
    shopping_cart.proceed_to_checkout()

    order_form = OrderForm(browser)
    order_form.select_gender_ms()
    order_form.enter_first_name('Maria')
    order_form.enter_last_name('Smith')
    order_form.enter_email('mariasmith@test.com')
    order_form.agree_to_terms_and_conditions()
    order_form.click_continue_button()

    delivery = OrderFormDelivery(browser)
    delivery.enter_address('123 Elms Street')
    delivery.enter_city('New Jersey')
    delivery.select_state('New York')
    delivery.enter_postal_code('25813')
    delivery.click_continue_button()

    shipping = OrderFormShipping(browser)
    shipping.enter_comment('Please leave package at door.')
    shipping.click_continue_button()
    payment = OrderFormPayment(browser)
    payment.pay_by_check()
    payment.agree_to_terms_and_conditions()
    payment.wait_for_order_button_to_load()
    payment.click_order_button()

























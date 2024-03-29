import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.go_to_cart
class TestGoToCart(object):
    def test_guest_cant_see_product_in_cart_opened_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_cart_page()
        page.should_not_be_product_in_cart()
        page.see_alert_about_empty_cart()


    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart_page()
        page.should_not_be_product_in_cart()
        page.see_alert_about_empty_cart()


def test_cart_is_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = CartPage(browser, link)
    page.open()
    page.should_not_be_product_in_cart()
    page.see_alert_about_empty_cart()


def test_cart_is_not_empty(browser):
    link = "http://selenium1py.pythonanywhere.com/basket/"
    page = CartPage(browser, link)
    page.open()
    page.should_be_product_in_cart()

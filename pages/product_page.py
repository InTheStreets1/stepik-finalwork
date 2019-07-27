from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def can_add_product_to_cart(self):
        self.should_be_button_add_product()
        self.add_product()
        self.get_promo_code()
        self.should_be_alert_about_added()
        self.should_be_alert_cart_total()

    def should_be_button_add_product(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_BUTTON), "Product button is not presented"

    def add_product(self):
        product_button = self.browser.find_element(
            *ProductPageLocators.PRODUCT_BUTTON)
        product_button.click()

    def get_promo_code(self):
        self.solve_quiz_and_get_code()

    def should_be_alert_about_added(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        assert self.is_element_present(
            *ProductPageLocators.ALLERT_ABOUT_ADD), "Alert about added is not presented"
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME).text
        alert = self.browser.find_element(
            *ProductPageLocators.ALLERT_ABOUT_ADD).text
        assert product_name in alert, "No product name in the alert"

    def should_be_alert_cart_total(self):
        assert self.is_element_present(
            *ProductPageLocators.ALERT_CART_TOTAL), "Alert cart total is not presented"
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        alert_cart_total = self.browser.find_element(
            *ProductPageLocators.ALERT_CART_TOTAL).text
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == alert_cart_total, "Price in cart is not equal to the product price"

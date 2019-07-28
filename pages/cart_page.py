from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def should_not_be_product_in_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.CART_ITEMS_FORMSET), "Product(s) in cart is presented, but should not be"

    def see_alert_about_empty_cart(self):
        assert self.is_element_present(
            *CartPageLocators.ALERT_EMPTY_CART), "Alert about empty cart is not presented"

    def should_be_product_in_cart(self):
        assert self.is_element_present(
            *CartPageLocators.CART_ITEMS_FORMSET), "No product(s) in cart presented, but chould be"


from selenium.webdriver.common.by import By


class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    CART_BUTTON = (By.CSS_SELECTOR, ".btn .btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators(object):
	LOGIN_FORM = (By.ID, "login_form")
	REG_FORM = (By.ID, "register_form")
	EMAIL_INPUT = (By.ID, "id_registration-email")
	PASSWORD_INPUT = (By.ID, "id_registration-password1")
	PASSWORD_X2_INPUT = (By.ID, "id_registration-password2")
	SUBMIT_BUTTON = (By.CSS_SELECTOR, ".btn .btn-lg .btn-primary")
	ALERT_REG_OK = (By.CSS_SELECTOR, "div.alertinner wicon")


class ProductPageLocators(object):
	PRODUCT_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
	PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
	ALLERT_ABOUT_ADD = (By.CSS_SELECTOR, "div.alertinner>strong")
	ALERT_CART_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")


class CartPageLocators(object):
    CART_ITEMS_FORMSET = (By.ID, "basket_formset")
    ALERT_EMPTY_CART = (By.ID, "content_inner")

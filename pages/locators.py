from selenium.webdriver.common.by import By


class BasePageLocators(object):
    INVALID = (By.ID, "invalid")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")


class ProductPageLocators(object):
    INVALID = (By.ID, "invalid")
    PRODUCT_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ALLERT_ABOUT_ADD = (By.CSS_SELECTOR, "div.alertinner>strong")
    ALERT_CART_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

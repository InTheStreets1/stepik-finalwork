import time
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.url, "Login url not presented"

    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REG_FORM), "Register form is not presented"

    def register_new_user(email, password):
        self.should_be_inputs()
        self.add_inputs()

    def should_be_inputs(self):
        assert self.is_element_present(
            *LoginPageLocators.EMAIL_INPUT), "Email input is not presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_INPUT), "Password input is not presented"
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_X2_INPUT), "Passwordx2 input is not presented"

    def add_inputs(self):
        email = str(time.time()) + "@fakemail.org"
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)

        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys("1235813aaa")

        passwordx2_input = self.browser.find_element(*LoginPageLocators.PASSWORD_X2_INPUT)
        passwordx2_input.send_keys("1235813aaa")

        assert self.is_element_present(*LoginPageLocators.ALERT_REG_OK, 'Registration error')

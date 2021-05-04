from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.url, "Not a login page url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME), \
            "Login: username textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), \
            "Login: password textbox is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_USERNAME), \
            "Reg: username textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS), \
            "Reg: password textbox is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS_CONFIRM), \
            "Reg: password confirm textbox is not presented"

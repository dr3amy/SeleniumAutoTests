from .base_page import BasePage
from .locators import ProductPageLocators
import pytest



class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_right_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product name not presented'
        elm1 = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_present(*ProductPageLocators.BASKET_PRODUCT_NAME), 'Basket product name not presented'
        elm2 = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text
        assert elm1 == elm2, 'Wrong product added to basket'

    def should_be_right_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'Product price not presented'
        price1 = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), 'Basket price not presented'
        price2 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert price1 == price2, 'Price is not equal'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared, but should be"




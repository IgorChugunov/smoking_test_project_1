import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_1 = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    select_product_2 = '//button[@id="add-to-cart-sauce-labs-bike-light"]'
    select_product_3 = '//button[@id="add-to-cart-sauce-labs-bolt-t-shirt"]'
    cart = '//a[@data-test="shopping-cart-link"]'
    menu_button = '//button[@id="react-burger-menu-btn"]'
    button_about = '//a[@id="about_sidebar_link"]'

    # Getters

    def get_product_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_product_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_product_3(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_cart(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_button_down_drop(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.button_about )))

     # Actions

    def click_select_product_1(self):
        self.get_product_1().click()
        print('Click select product 1')

    def click_select_product_2(self):
        self.get_product_2().click()
        print('Click select product 2')

    def click_select_product_3(self):
        self.get_product_3().click()
        print('Click select product 3')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    def click_button_menu(self):
        self.get_button_down_drop().click()
        print('Click MENU')

    def click_button_about(self):
        self.get_menu_button().click()
        print('Click about')
    # Methods
    def select_products_1(self):
        self.get_current_url()
        self.click_select_product_1()
        self.click_cart()
    def select_products_2(self):
        self.get_current_url()
        self.click_select_product_2()
        self.click_cart()

    def select_products_3(self):
        self.get_current_url()
        self.click_select_product_3()
        self.click_cart()


    def select_menu_about(self):
        with allure.step("Select menu about"):
            Logger.add_start_step(method='select_menu_about')
            self.get_current_url()
            self.click_button_menu()
            self.click_button_about()
            self.assert_url('https://saucelabs.com/')
            Logger.add_end_step(url=self.driver.current_url, method='select_menu_about')
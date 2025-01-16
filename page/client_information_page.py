import time

import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = '//input[@id="first-name"]'
    last_name = '//input[@id="last-name"]'
    postal_code = '//input[@id="postal-code"]'
    continue_button = '//input[@id="continue"]'

    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

     # Actions

    def input_first_name(self, name_first):
        self.get_first_name().send_keys(name_first)
        print('Input first name')

    def input_last_name(self, name_last):
        self.get_last_name().send_keys(name_last)
        print('Input last name')

    def input_postal_code(self, postal):
        self.get_postal_code().send_keys(postal)
        print('Input postal code')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue button')

    # Methods
    def client_infromation(self):
        with allure.step("Client infromation"):
            Logger.add_start_step(method='client_infromation')
            self.get_current_url()
            self.input_first_name("Козел")
            self.input_last_name("Тёмный")
            self.input_postal_code('123456')
            self.click_continue_button()
            Logger.add_end_step(url=self.driver.current_url, method='client_infromation')
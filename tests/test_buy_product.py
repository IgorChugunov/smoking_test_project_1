"""Открываем браузер в тестовом режиме"""
import time

import pytest
from selenium.webdriver.support import expected_conditions as EC
import allure
from page.cart_page import Cart_page
from page.client_information_page import Client_information_page
from page.finish_page import Finish_page
from page.login_page import Login_page
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

from page.main_page import Main_page
from page.payment_page import Payment_page


@allure.description("Test buy product 1")
def test_buy_product_1():
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()
    print('Start_test')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()
    cp = Cart_page(driver)
    cp.click_checkout_button()
    cip = Client_information_page(driver)
    cip.client_infromation()
    p = Payment_page(driver)
    p.payment()
    f = Finish_page(driver)
    f.finish()




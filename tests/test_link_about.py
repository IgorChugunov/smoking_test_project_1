
"""Открываем браузер в тестовом режиме"""
import time

from selenium.webdriver.support import expected_conditions as EC

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


def test_link_product():
    option = Options()
    option.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome()
    print('Start_test')

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_menu_about()
    print('Start_finish')

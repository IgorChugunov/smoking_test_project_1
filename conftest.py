import pytest
from selenium import webdriver


@pytest.fixture()
def set_up():
    print("Start test")
    yield
    print('Finish test')


@pytest.fixture(scope="module")
def set_group():
    print("ENTER system")
    yield
    print('Exit system')

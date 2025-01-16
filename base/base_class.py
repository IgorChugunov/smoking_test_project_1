import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Methods get current url"""
    def get_current_url(self):
        get_url =self.driver.current_url
        print('Current url ' + get_url)

    """Methods assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Result word good")

    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\User\\Documents\\PycharmProjects\\main_project\\screen\\' + name_screenshot)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Correct url')
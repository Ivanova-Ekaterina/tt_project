import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/ekaterina/Downloads/chromedriver')

    def test_search_element(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/login/")
        full_name = driver.find_element_by_id("full_name")
        assert full_name is not None
        full_name.send_keys('John Smith')
        user_nickname = driver.find_element_by_id("user_nickname")
        assert user_nickname is not None
        user_nickname.send_keys('Johny')
        button = driver.find_element_by_id("auth")
        assert button is not None
        time.sleep(3)
        button.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

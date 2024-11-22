import time
import unittest

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class base_test(unittest.TestCase):
    def setUp(self):
        service = Service("C:\\Drivers2\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")

    def tearDown(self):
        self.driver.close()
        time.sleep(4)


if __name__== '__main__':
    unittest.main()
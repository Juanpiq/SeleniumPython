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


class PruebaLogin(unittest.TestCase):
    def setUp(self):
        service = Service("C:\\Drivers2\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        #self.driver.maximize_window()

    def test_login1(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nom.send_keys("Juan")
        clave.send_keys("admin123")
        bt.click()
        error = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(@data-test,'error')]")))
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)
        if error == "Epic sadface: Username and password do not match any user in this service":
            print("Los datos no son correctos")
            print("Prueba uno Ok")
        time.sleep(2)

    def test_login2(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nom.send_keys("")
        clave.send_keys("admin123")
        bt.click()
        error = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, "//h3[contains(@data-test,'error')]")))
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)
        if error == "Epic sadface: Username is required":
            print("Falta el username")
            print("Prueba dos Ok")
        time.sleep(2)

    def test_login3(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nom.send_keys("Juan")
        clave.send_keys("")
        bt.click()
        error = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(@data-test,'error')]")))
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)
        if error == "Epic sadface: Password is required":
            print("Falta el password")
            print("Prueba tres Ok")
        time.sleep(2)

    def test_login4(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nom.send_keys("")
        clave.send_keys("")
        bt.click()
        error = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[contains(@data-test,'error')]")))
        error = driver.find_element(By.XPATH, "//h3[contains(@data-test,'error')]")
        error = error.text
        print(error)
        if error == "Epic sadface: Username is required":
            print("Faltan ambos campos")
            print("Prueba cuatro pendiente")
        time.sleep(2)

    def test_login5(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        nom = driver.find_element(By.XPATH, "//input[contains(@id,'user-name')]")
        clave = driver.find_element(By.XPATH, "//input[contains(@id,'password')]")
        bt = driver.find_element(By.XPATH, "//input[contains(@id,'login-button')]")

        nom.send_keys("standard_user")
        clave.send_keys("secret_sauce")
        bt.click()

        elemento = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")))
        elemento = driver.find_element(By.XPATH, "//div[@class='app_logo'][contains(.,'Swag Labs')]")
        print(elemento.is_displayed())

        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__== '__main__':
    unittest.main()
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
from Funciones.Funciones import Funciones_Globales
from Funciones.Page_Login import Pagina_Login

t = .5
class base_test(unittest.TestCase):
    def setUp(self):
        service = Service("C:\\Drivers2\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        pg = Pagina_Login(driver)
        pg.Login_Master("https://www.saucedemo.com/", "Juan", "Admin123", t)

    def test2(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", t)
        f.Upload_Xpath("//input[@id='uploadPicture']","C:\\Users\\djpab\\PycharmProjects\\Curso_selenium\\imagenes\\deku.jpg", 3)

    def test3(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", t)
        f.Check_Xpath("//label[contains(.,'Sports')]", t)

    def test4(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar("https://demoqa.com/automation-practice-form", t)
        #f.Check_Xpath_Multiple(t, "//label[@for='hobbies-checkbox-1']", "//label[@for='hobbies-checkbox-2']", "//label[@for='hobbies-checkbox-3']")
        for n in range(1,4):
            f.Check_Xpath_Multiple(t, "//label[@for='hobbies-checkbox-"+str(n)+"']")

    def tearDown(self):
        self.driver.close()
        time.sleep(4)


if __name__== '__main__':
    unittest.main()
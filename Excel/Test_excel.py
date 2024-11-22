import time
import unittest
from Funciones_Ex import *

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Funciones.Funciones import Funciones_Globales

tg = 1

class base_test(unittest.TestCase):

    def setUp(self):
        service = Service("C:\\Drivers2\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def test1(self):
        driver = self.driver
        f = Funciones_Globales(driver)
        fe = Funexcel(driver)
        f.Navegar("https://demoqa.com/text-box", tg)
        ruta ="C:\\Users\\djpab\\Documents\\CURSOS\\Selenium\\Selenium_python\\practicas_excel\\Datos_ok.xlsx"
        filas = fe.getRowCount(ruta, "Sheet1")

        for r in range(2, filas+1):
            nombre = fe.readData(ruta, "Sheet1", r, 1)
            email = fe.readData(ruta, "Sheet1", r,2)
            dir1 = fe.readData(ruta, "Sheet1", r, 3)
            dir2 = fe.readData(ruta, "Sheet1", r, 4)

            f.Texto_Mixto("id", "userName", nombre, tg)
            f.Texto_Mixto("id", "userEmail", email, tg)
            f.Texto_Mixto("id", "currentAddress", dir1, tg)
            f.Texto_Mixto("id", "permanentAddress", dir2, tg)
            f.Click_Mixto("id", "submit", tg)

            e = f.Existe("id", "name", tg)
            if(e == "Existe"):
                print("El elemento se insertó correctamente")
                fe.writeData(ruta, "Sheet1", r, 5, "Insertado")
            else:
                print("No se insertó")
                fe.writeData(ruta, "Sheet1", r, 5, "Error")
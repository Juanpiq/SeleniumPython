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



class Pagina_Login():

    def __init__(self, driver):
        self.driver = driver

    def Login_Master(self, url, name, clave, t):
        driver = self.driver
        f = Funciones_Globales(driver)
        f.Navegar(url, t)
        f.Texto_Mixto("xpath","//input[contains(@id,'user-name')]", name, t)
        f.Texto_Mixto("xpath","//input[contains(@id,'password')]", clave, t)
        f.Click_Mixto("xpath","//input[contains(@id,'login-button')]", t)
        f.Salida()
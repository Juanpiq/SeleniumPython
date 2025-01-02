import time
import unittest
from tkinter.tix import Select

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Funciones_Globales():

    def __init__(self, driver):
        self.driver = driver

    def Tiempo(self, tie):
        t = time.sleep(tie)
        return t

    def Navegar(self, url, Tiempo):
        self.driver.get(url)
        self.driver.maximize_window()
        t = time.sleep(Tiempo)
        return t

    def SEX(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.XPATH, elemento)
        return val

    def SEI(self, elemento):
        val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, elemento)))
        val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
        val = self.driver.find_element(By.ID, elemento)
        return val

    def Texto_Mixto(self, tipo, selector, texto, Tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

    def Click_Mixto(self, tipo, selector, Tiempo):
        if (tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif (tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)


    def Select_Mixto_Type(self, indicador,selector, tipo, dato, Tiempo):
        if(indicador == "xpath"):
            try:
                val = self.SEX(selector)
                val = Select(val)
                if (tipo == "text"):
                    val.select_by_visible_text(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                elif (tipo == "value"):
                    val.select_by_value(dato)

                print("El campo Seleccionado es {}".format(dato))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(indicador == "id"):
            try:
                val = self.SEI(selector)
                val = Select(val)
                if (tipo == "text"):
                    val.select_by_visible_text(dato)
                elif (tipo == "index"):
                    val.select_by_index(dato)
                elif (tipo == "value"):
                    val.select_by_value(dato)

                print("El campo Seleccionado es {}".format(dato))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)


    def Upload_Mixto(self, tipo, selector,ruta, Tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.send_keys(ruta)
                print("Se carga la imagen {}".format(ruta))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val.send_keys(ruta)
                print("Se carga la imagen {}".format(ruta))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

    def Check_Mixto(self, tipo, selector, Tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                val.click()
                print("Click en el elemento {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                val.click()
                print("Click en el elemento {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

    def Check_Mixto_Multiple(self, tipo, Tiempo, *args):
        for x in args:
            self.Check_Mixto(tipo, x, Tiempo)

    def Existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                print("Click en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)
                return "No Existe"

        elif(tipo == "id"):
            try:
                val = self.SEX(selector)
                print("Click en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)
                return "No Existe"


    def Mouse_Doble(self, tipo, selector, Tiempo = 2):
        if(tipo == "xpath"):
            try:
                val = self.SEX(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = self.SEI(selector)
                act = ActionChains(self.driver)
                act.double_click(val).perform()
                print("DoubleClick en {}".format(selector))
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

    def Salida(self):
        print("Se termina la prueba exitosamente")
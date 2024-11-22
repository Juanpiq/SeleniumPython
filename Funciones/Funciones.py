import time
import unittest
from tkinter.tix import Select

from selenium import webdriver
from selenium.common import TimeoutException
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

    def Texto_Mixto(self, tipo, selector, texto, Tiempo):
        if(tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                val.clear()
                val.send_keys(texto)
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
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
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)

        elif (tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                val.click()
                t = time.sleep(Tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)


    def Select_Xpath_Text(self, xpath, texto, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            val.select_by_visible_text(texto)
            print("El campo seleccionado es {}".format(texto))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + xpath)



    def Select_Xpath_Type(self, xpath, tipo, dato, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)

            print("El campo Seleccionado es {}".format(dato))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + xpath)

    def Select_ID_Type(self, id, tipo, dato, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.ID, id)
            val = Select(val)
            if(tipo == "text"):
                val.select_by_visible_text(dato)
            elif(tipo == "index"):
                val.select_by_index(dato)
            elif(tipo == "value"):
                val.select_by_value(dato)

            print("El campo Seleccionado es {}".format(dato))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + id)

    def Upload_Xpath(self, xpath, ruta, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + xpath)

    def Upload_ID(self, id, ruta, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, id)
            val.send_keys(ruta)
            print("Se carga la imagen {}".format(ruta))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + id)

    def Check_Xpath(self, xpath, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, xpath)
            val.click()
            print("Click en el elemento {}".format(xpath))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + xpath)

    def Check_ID(self, id, Tiempo):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
            val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
            val = self.driver.find_element(By.XPATH, id)
            val.click()
            print("Click en el elemento {}".format(id))
            t = time.sleep(Tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontró el Elemento" + id)

    def Check_Xpath_Multiple(self, Tiempo, *args):
        for num in args:
            self.Check_Xpath(num, Tiempo)

    def Existe(self, tipo, selector, tiempo):
        if(tipo == "xpath"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.XPATH, selector)
                print("Click en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)
                return "No Existe"

        elif(tipo == "id"):
            try:
                val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, selector)))
                val = self.driver.execute_script("arguments[0].scrollIntoView();", val)
                val = self.driver.find_element(By.ID, selector)
                print("Click en el elemento {}".format(selector))
                t = time.sleep(tiempo)
                return "Existe"
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontró el Elemento" + selector)
                return "No Existe"

    def Salida(self):
        print("Se termina la prueba exitosamente")
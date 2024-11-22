import time
from sys import executable

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support.ui import  Select
from selenium.webdriver.support import expected_conditions as EC

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\Drivers2\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://pixabay.com/es/")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
t = 0.1

#driver.execute_script("window.scrollTo(0,1000)")

try:

    Buscar= WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")))
    Buscar = driver.find_element(By.XPATH, "//span[@class='label--Ngqjq'][contains(.,'Descubre más')]")
    ir = driver.execute_script("arguments[0].scrollIntoView();", Buscar)
    Buscar.click()
    time.sleep(t)
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible")


time.sleep(t)
driver.close()
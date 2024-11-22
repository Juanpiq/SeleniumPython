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
service = Service("C:\Drivers2\chromedriver-win64\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://testpages.herokuapp.com/styled/file-upload-test.html")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
driver.implicitly_wait(10)
t = 3

try:

    Buscar= WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'fileinput')]")))
    Buscar = driver.find_element(By.XPATH,"//input[contains(@id,'fileinput')]")
    Buscar.send_keys("C:\\Users\\djpab\\PycharmProjects\\Curso_selenium\\imagenes\\deku.jpg")
    time.sleep(t)
    driver.find_element(By.XPATH, "//input[contains(@id,'itsanimage')]").click()
    driver.find_element(By.XPATH, "//input[contains(@type,'submit')]").click()


except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible")

time.sleep(t)
driver.close()
import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\Drivers2\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
time.sleep(1)

nom = driver.find_element(By.CSS_SELECTOR, "#userName")
nom.send_keys("Juan")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#userEmail").send_keys("juan@gmail.com")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("Lorem ipsum")
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#permanentAddress").send_keys("Direccion permanente")
time.sleep(1)

driver.execute_script("window.scroll(0,500)")
time.sleep(2)

driver.find_element(By.ID, "submit").click()
time.sleep(1)

driver.close()
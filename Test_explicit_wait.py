import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\Drivers2\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
driver.implicitly_wait(10)
t = 3
btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "")))
btn.click

driver.close()
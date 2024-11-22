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

nom = driver.find_element(By.XPATH, "//input[@type='text' and @ID='userName']")
nom.send_keys("Juan")
nom.send_keys(Keys.TAB + "juan@gmail.com" + Keys.TAB + "lorem ipsum" + Keys.TAB + "Direccion permamente" + Keys.TAB + Keys.ENTER)

driver.execute_script("window.scrollTo(0,300)")
time.sleep(4)

driver.close()
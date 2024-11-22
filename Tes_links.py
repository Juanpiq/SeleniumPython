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
from selenium.webdriver.common.action_chains import ActionChains

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\Drivers2\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/links")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
#driver.implicitly_wait(10)
t = 0.1

link2 = driver.find_element(By.XPATH, "//a[@href='javascript:void(0)'][contains(.,'No Content')]")
ir = driver.execute_script("arguments[0].scrollIntoView();", link2)

links = driver.find_elements(By.TAG_NAME, "a")

print("El numero de links que hay en la página es de ", len(links))

for num in links:
    print(num.text)

driver.find_element(By.LINK_TEXT, "Home").click()
time.sleep(3)
time.sleep(t)
driver.close()
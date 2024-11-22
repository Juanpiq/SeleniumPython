import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\\Drivers2\\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://demoqa.com/")
driver.maximize_window()  # Hace que abra la pestaña en pantalla completa
t = 0.1

titulo = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
print(titulo.is_displayed())
btn1 = driver.find_element(By.XPATH, "(//div[contains(@class,'card-up')])[1]")
ir = driver.execute_script("arguments[0].scrollIntoView();", btn1)

if titulo.is_displayed():
    print("Existe la imagen")
    btn1.click()
    time.sleep(2)
else:
    print("No existe la imagen")

time.sleep(t)
driver.close()
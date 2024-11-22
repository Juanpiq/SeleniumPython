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

driver.get("https://demoqa.com/text-box")
driver.maximize_window()  # Hace que abra la pestaña en pantalla completa
t = 0.1

btn1 = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
ir = driver.execute_script("arguments[0].scrollIntoView();", btn1)
time.sleep(2)
print(btn1.is_enabled())

if btn1.is_enabled():
    print("Puedes dar click")
else:
    print("No puedes dar click")


time.sleep(t)
driver.close()
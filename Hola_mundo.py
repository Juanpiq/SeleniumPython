from sys import executable

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Especifica la ruta al chromedriver usando 'Service'
service = Service("C:\Drivers2\chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.get("https://demoqa.com/text-box")

print("Bienvenido a Selenium")
print(driver.title)

driver.close()
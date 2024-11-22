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

driver.get("https://demoqa.com/modal-dialogs")
driver.maximize_window()  # Hace que abra la pestaña en pantalla completa
t = 0.1

#driver.switch_to.alert.accept()  casi no se usan porque es posible que el elmento sea definido con otro nombre
#driver.switch_to.alert.dismiss()


try:
    # Haz clic en el botón para mostrar el modal
    botonModal = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id,'showSmallModal')]"))
    )
    ir = driver.execute_script("arguments[0].scrollIntoView();", botonModal)
    botonModal.click()
    time.sleep(2)

    # Espera a que aparezca el botón para cerrar el modal y haz clic en él
    botonClose = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@id,'closeSmallModal')]"))
    )
    botonClose.click()

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible")

time.sleep(t)
driver.close()
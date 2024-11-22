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

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window() #hace que abra la pestaña en pantalla completa
#driver.implicitly_wait(10)
t = 0.1

try:
    insertar= WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//input[contains(@id,'firstName')]")))
    insertar = driver.find_element(By.XPATH,"//input[contains(@id,'firstName')]")
    insertar.send_keys("Juan" + Keys.TAB + "Navarro" + "jpablonav@gmail.com")
except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no está disponible")

gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1'][contains(.,'Male')]")
ir = driver.execute_script("arguments[0].scrollIntoView();", gender)
gender.click()

mobile = driver.find_element(By.XPATH, "//input[contains(@id,'userNumber')]")
mobile.send_keys("0123456789")

calendario = driver.find_element(By.XPATH,"//input[contains(@id,'dateOfBirthInput')]")
calendario.click()

yearSelect = driver.find_element(By.XPATH,"//select[contains(@class,'react-datepicker__year-select')]")
year = Select(yearSelect)
year.select_by_visible_text("2019")

mesSelect = driver.find_element(By.XPATH,"//select[contains(@class,'react-datepicker__month-select')]")
mes = Select(mesSelect)
mes.select_by_index(0)


try:
    dia = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--015'][contains(.,'15')]")))
    dia.click()

except TimeoutException as ex:
    print(ex.msg)
    print("No se encuentra el dia")


subjects = driver.find_element(By.ID,"subjectsInput")
subjects.send_keys("English")
time.sleep(1)
subjects.send_keys(Keys.ENTER)

subjects.send_keys("Maths")
time.sleep(1)
subjects.send_keys(Keys.ENTER)


sports = driver.find_element(By.XPATH,"//label[@for='hobbies-checkbox-1'][contains(.,'Sports')]")
sports.click()

music = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-3'][contains(.,'Music')]")
music.click()

upfile = driver.find_element(By.XPATH, "//input[contains(@id,'uploadPicture')]")
upfile.send_keys("C:\\Users\\djpab\\PycharmProjects\\Curso_selenium\\imagenes\\deku.jpg")

address = driver.find_element(By.XPATH,"//textarea[contains(@id,'currentAddress')]")
address.send_keys("Insertando direccion")

stateSelect = driver.find_element(By.ID, "react-select-3-input")
ir1 = driver.execute_script("arguments[0].scrollIntoView();", stateSelect)
stateSelect.send_keys("Haryana")
time.sleep(1)
stateSelect.send_keys(Keys.ENTER)

time.sleep(1)

citySelect = driver.find_element(By.ID, "react-select-4-input")
citySelect.send_keys("Karnal")
time.sleep(1)
citySelect.send_keys(Keys.ENTER)

submit = driver.find_element(By.XPATH, "//button[contains(@id,'submit')]")
ir2 = driver.execute_script("arguments[0].scrollIntoView();", submit)
submit.click()

try:
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "modal-body")))
    print("Modal visible: Formulario enviado correctamente.")
    cerrar_boton = driver.find_element(By.XPATH, "//button[contains(@id,'closeLargeModal')]")
    ir3 = driver.execute_script("arguments[0].scrollIntoView();", cerrar_boton)
    ActionChains(driver).move_to_element(cerrar_boton).click(cerrar_boton).perform()
    time.sleep(4)

except TimeoutException:
    print("El modal de confirmación no apareció.")


time.sleep(3)
time.sleep(t)
driver.close()
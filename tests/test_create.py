from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#PRUEBA FELIZ
driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

driver.find_element(By.ID, "nombre").send_keys("Juan Perez")
driver.find_element(By.ID, "email").send_keys("juan@gmail.com")
driver.find_element(By.ID, "btnCrear").click()

driver.save_screenshot("tests/create_feliz.png")
print("Prueba feliz ejecutada")

time.sleep(2)

#PRUEBA NEGATIVA
driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

driver.find_element(By.ID, "nombre").send_keys("Juan")
driver.find_element(By.ID, "email").send_keys("correo_mal")
driver.find_element(By.ID, "btnCrear").click()

driver.save_screenshot("tests/create_negativa.png")
print("Prueba negativa ejecutada")

time.sleep(2)

#PRUEBA DE LÍMITE
driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

driver.find_element(By.ID, "nombre").send_keys("")
driver.find_element(By.ID, "email").send_keys("test@gmail.com")
driver.find_element(By.ID, "btnCrear").click()

driver.save_screenshot("tests/create_limite.png")
print("Prueba de límite ejecutada")

time.sleep(2)

driver.quit()
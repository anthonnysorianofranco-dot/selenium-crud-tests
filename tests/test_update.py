from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

# Crear usuario primero
driver.find_element(By.ID, "nombre").send_keys("Carlos")
driver.find_element(By.ID, "email").send_keys("carlos@gmail.com")
driver.find_element(By.ID, "btnCrear").click()

time.sleep(2)

# Click en editar
driver.find_element(By.ID, "editBtn").click()

time.sleep(2)

# Limpiar y actualizar
nombre = driver.find_element(By.ID, "nombre")
nombre.clear()
nombre.send_keys("Carlos Actualizado")

email = driver.find_element(By.ID, "email")
email.clear()
email.send_keys("carlos_update@gmail.com")

driver.find_element(By.ID, "btnUpdate").click()

driver.save_screenshot("tests/update.png")

print("Usuario actualizado correctamente")

time.sleep(2)
driver.quit()
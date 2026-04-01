from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Abrir navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Ir a tu CRUD
driver.get("http://localhost/selenium-crud-tests/index.php")

print("Página abierta correctamente")

time.sleep(3)

driver.quit()

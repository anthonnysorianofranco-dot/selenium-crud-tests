from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

driver.save_screenshot("tests/delete.png")
print("Prueba de eliminación ejecutada")

driver.quit()
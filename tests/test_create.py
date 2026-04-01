from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("http://localhost/selenium-crud-tests/index.php")
time.sleep(2)

driver.find_element(By.ID, "nombre").send_keys("Juan Perez")
driver.find_element(By.ID, "email").send_keys("juan@gmail.com")
driver.find_element(By.ID, "btnCrear").click()

driver.save_screenshot("tests/create_feliz.png")

time.sleep(2)
driver.quit()
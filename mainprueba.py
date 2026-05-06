from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver= webdriver.Chrome()

wait= WebDriverWait(driver,10)

driver.get("https://www.google.com")
print("Probando si el entorno y Selenium funcionan...")

input_buscador= driver.find_element(By.NAME, "q")
input_buscador.send_keys("talento tech")
input_buscador.send_keys(Keys.RETURN)
time.sleep(4) #esto mas adelante se borra
driver.quit()



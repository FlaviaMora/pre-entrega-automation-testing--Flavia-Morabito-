#inicializar web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#traer manager y servicios de acuerdo a mi navegador

def get_driver():
    #instalar el driver del navegador correcto, pasarle a una instancia ara q lo pueda almacenar
    driver= webdriver.Chrome()
    return driver

def login(driver,username, password):
    wait= WebDriverWait(driver, 10)
    driver.get("https://saucedemo,com/")
    wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
    ).send_keys(username)

    driver.find_element(By.ID, "password").send_Keys(password)
    driver.find_element(By.ID, "login-button").click()
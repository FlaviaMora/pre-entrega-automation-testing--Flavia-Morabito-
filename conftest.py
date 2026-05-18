import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")

def driver():
#Fixture que proporciona un WebDriver configurado
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    time.sleep(1) # Para ver el resultado final
    driver.quit()

from pages.login_page import LoginPage

@pytest.fixture
def credenciales_validas():
    return {"usuario": "standard_user", "clave": "secret_sauce"}

@pytest.fixture
def usuario_logueado(driver, credenciales_validas):
    """Realiza el login automáticamente y deja al usuario en el inventario."""
    login_page = LoginPage(driver)
    login_page.abrir().login_completo(
        credenciales_validas["usuario"], 
        credenciales_validas["clave"]
    )
    return driver    
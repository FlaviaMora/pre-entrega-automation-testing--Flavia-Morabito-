from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_login(driver):
    login(driver,"standard_user","secret_sauce")
    assert "inventory.html" in driver.current_url #poner la url completa del catalogo
    title= driver.find_element(By.CLASS_NAME, "title").text #el titulo se puede poner en otra funcion
    assert title== "Products"


def test_catalogo(driver):
    login(driver, "standart_user", "secret_user")
    title= driver.find_element(By.CLASS_NAME, "title").text #el titulo se puede poner en otra funcion
    assert title== "Products"
    #validar productos
    productos= driver.find_elements(By.CSS_SELECTOR, "[data-test= 'inventory-item']")
    assert len(productos) > 0

    nombre=productos[0].find_element(By.CLASS_NAME, "inventory- item-name")
    assert nombre=="Sauce Labs Bacpack"

def test_agregar_al_carrito(driver):
    login(driver, "standart_user, "secret_sauce")
    #agregar producto
    wait= WebDriver(driver, 10)

    nombre_producto=driver.find_element(By.CLASS_NAME, "inventory--item-name").text
    btn_add=wait.untill(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text().'Add to cart')]"))
    )
    btn_add.click()

    #verificar contador
    badge= driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text== "1"

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
#que cambie el carrito, que se agrego elemento
    producto_en_carrito=driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_en_carrito==nombre_producto

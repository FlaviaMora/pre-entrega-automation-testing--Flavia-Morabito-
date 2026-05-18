from selenium.webdriver.common.by import By

class CartPage:
    
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver

    def obtener_nombres_productos_en_carrito(self):
        """Devuelve una lista con los nombres de todos los productos en el carrito."""
        # Busca todos los elementos que tengan ese nombre
        elementos = self.driver.find_elements(*self._CART_ITEM_NAME)
        
        # Extraer el texto de cada elemento y guardarlo en una lista
        nombres = []
        for elemento in elementos:
            nombres.append(elemento.text)    
        return nombres
    
    def verificar_pagina_carrito(self):
        """Verifica que la URL sea la del carrito."""
        return "cart.html" in self.driver.current_url

    def volver_al_inventario(self):
        """Hace clic en seguir comprando y retorna al inventario."""
        self.driver.find_element(*self._CONTINUE_SHOPPING_BTN).click()
        from pages.inventory_page import InventoryPage
        return InventoryPage(self.driver)

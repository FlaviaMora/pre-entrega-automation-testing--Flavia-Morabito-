import pytest
from pages.inventory_page import InventoryPage

class TestCart:

    @pytest.mark.smoke
    @pytest.mark.carrito
    def test_agregar_producto_al_carrito(self, usuario_logueado):
        """Verifica el flujo completo de agregar un ítem y verlo en el carrito."""
        
        inventory_page = InventoryPage(usuario_logueado)
        
        # Guardar el nombre del primer producto en una variable
        nombre_esperado = inventory_page.obtener_nombre_primer_producto()
        
        inventory_page.agregar_primer_producto()
        
        assert inventory_page.obtener_contador_carrito() == 1, "El contador del carrito no subió a 1"
    
        cart_page = inventory_page.ir_al_carrito()
        
        # Validar que la URL haya cambiado a la del carrito
        assert cart_page.verificar_pagina_carrito(), "Error: No se redirigió a la URL del carrito"
        
        productos_comprados = cart_page.obtener_nombres_productos_en_carrito()
        
        # Verificar que esté en la lista
        assert nombre_esperado in productos_comprados, f"Error: '{nombre_esperado}' no se encontró en el carrito"
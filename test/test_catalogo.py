import pytest
from pages.inventory_page import InventoryPage

class TestCatalogo:

    @pytest.mark.catalogo
    def test_verificar_catalogo_base(self, usuario_logueado):
        """Verifica que el catálogo cargue correctamente y muestre los productos."""
        
        inventory_page = InventoryPage(usuario_logueado)
        
        # (Asserts)
        # Validar que el título sea correcto
        titulo_actual = inventory_page.obtener_titulo()
        assert titulo_actual == "Products", f"Error: El título fue '{titulo_actual}'"
        
        # Comprobar que existan productos visibles (que la lista sea mayor a 0)
        productos = inventory_page.obtener_productos()
        assert len(productos) > 0, "Error: No se cargó ningún producto en la pantalla"
        
        # Validar el nombre y precio del primer producto
        nombre_primero = inventory_page.obtener_nombre_primer_producto()
        precio_primero = inventory_page.obtener_precio_primer_producto()
        
        # Verificar que no vengan como textos vacíos
        assert nombre_primero != "", "Error: El nombre del primer producto está vacío"
        assert precio_primero != "", "Error: El precio del primer producto está vacío"
        
        #Imprime en consola qué producto encontró
        print(f"\n Producto encontrado: {nombre_primero} | Precio: {precio_primero}")
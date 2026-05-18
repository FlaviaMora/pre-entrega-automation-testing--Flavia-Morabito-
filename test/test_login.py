import pytest
from pages.login_page import LoginPage
from data.users import USERS

class TestLogin:

    @pytest.mark.parametrize("usuario, clave", USERS)
    def test_login_parametrizado(self, driver, usuario, clave):
        """Prueba el login con todos los usuarios de users.py"""
        login_page = LoginPage(driver)
        login_page.abrir().login_completo(usuario, clave)
        
        if usuario == "locked_out_user":
            #validar que aparezca el mensaje en rojo
            assert login_page.esta_error_visible(), "El error no apareció para el usuario bloqueado"
            
            #validar que el mensaje contenga "locked out"
            mensaje_actual = login_page.obtener_mensaje_error()
            assert "locked out" in mensaje_actual, f"Mensaje incorrecto. Se obtuvo: '{mensaje_actual}'"
            
        else:
            # El resto de los usuarios deberían entrar al inventario
            assert "inventory.html" in driver.current_url, f"El usuario {usuario} no fue redirigido. URL: {driver.current_url}"
            assert driver.title == "Swag Labs", f"El título no es correcto para el usuario {usuario}"
# pre-entrega-automation-testing

Autor: Flavia Morabito
**Repositorio:** https://github.com/FlaviaMora/pre-entrega-automation-testing--Flavia-Morabito-.git

Propósito del Proyecto
Este proyecto es la pre entrega de automatización de pruebas de saucedemo.com. Su objetivo es validar los flujos críticos (Login, Catálogo y Carrito) implementando el patrón de diseño Page Object Model (POM).

Tecnologías Utilizadas
* Python 3.14.3
* Selenium WebDriver
* Pytest (Framework de pruebas)
* Pytest-HTML (Reportes)

Cómo instalar las dependencias
1. Clonar el repositorio.
2. Crear y activar un entorno virtual (`python -m venv venv`).
3. Instalar dependencias: `pip install -r requirements.txt`

Cómo ejecutar las pruebas y generar el reporte
Para correr todas las pruebas y generar un reporte visual con los resultados, ejecutá el siguiente comando en la terminal:
```bash
pytest test/ -v --html=reporte.html --self-contained-html

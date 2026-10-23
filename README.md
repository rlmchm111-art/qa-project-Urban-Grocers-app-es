# Proyecto Urban Grocers

## Descripción
Pruebas automatizadas de API para la aplicación Urban Grocers. Se comprueba la creación de kits de productos (`POST /api/v1/kits`) y, en concreto, la validación del campo `name`, siguiendo una lista de comprobación de 9 pruebas.

## Documentación utilizada
La documentación de la API del servidor de Urban Grocers, disponible en la ruta `/docs/` del servidor (sección Main.Kits, "Crear un kit").

## Tecnologías y técnicas utilizadas
- Python 3
- pytest, para escribir y ejecutar las pruebas
- requests, para enviar las solicitudes HTTP
- Pruebas positivas (código 201) y negativas (código 400)
- Git y GitHub para el control de versiones

## Estructura del proyecto
- `configuration.py`: URL del servidor y rutas de la API
- `data.py`: cuerpos de las solicitudes
- `sender_stand_request.py`: funciones que envían las solicitudes
- `create_kit_name_kit_test.py`: las pruebas
- `.gitignore`: archivos que Git debe ignorar

## Cómo ejecutar las pruebas
1. Instala las dependencias con `pip install pytest requests`.
2. Inicia el servidor de Urban Grocers y copia su URL.
3. Pega la URL en la variable `URL_SERVICE` de `configuration.py`.
4. Ejecuta las pruebas con `pytest create_kit_name_kit_test.py`.

Algunas pruebas pueden mostrar FAILED porque la API no valida ciertos casos; es un resultado esperado dentro de la lista de comprobación.

# Documentación de APIs.
Todas las APIs de archivos .json están escritas de tal manera que al ingresarlas en SwaggerUI se pueda visualizar su comportamiento de una manera más simple y amigable.
## - Visualización en SwaggerUI.
**0)** Dado que las APIs no están desplegadas en una url propia, para poder ingresarlas en Swagger deberemos copiar sus líneas desde este repositorio y pegarlo en un archivo vacío en el editor de Swagger.

**1)** Dirigete a [SwaggerEditor](https://editor.swagger.io/).

**2)** En el menú de opciones superior, selecciona la opción *File > Clear editor*.

**3)** Luego, dentro del archivo de la API de este repositorio que quieres visualizar. En la barra de opciones arriba del código, clickea en *Copy raw file*.

**4)** Por último, pega las lineas de la API en el archivo vacío que generó Swagger en el lado izquierdo de la web.

* #### En este punto el editor de Swagger mostrará en el lado izquierdo de la página el archivo .json, y en la parte derecha las distintas operaciones que proporciona la API, con sus respectivas descripciones y ejemplos para cada caso. 
Este repositorio contiene el código para convertir ficciones de Autorol 3.0 (https://natilla.comunidadumbria.com/autorol/) en aplicaciones Android.


REQUISITOS INFORMÁTICOS

- Sistema operativo Windows.
  
- Python (el código fue escrito y probado en Python 3.12 pero debería funcionar también en versiones anteriores). INSTALA PYTHON: https://www.python.org/downloads/
  
- Una IDE (yo usé VSCode). INSTALA VSCODE: https://code.visualstudio.com/download
  
- La herramienta Kivy (el código fue escrito en la version 2.3.0). INSTALA KIVY: https://kivy.org/doc/stable/gettingstarted/installation.html#install-kivy TUTORIAL SOBRE USAR KIVY: https://www.youtube.com/watch?v=l8Imtec4ReQ

- Windows Subsystem for Linux version 2 (WSL2). TUTORIAL SOBRE COMO INSTALARLO: https://www.youtube.com/watch?v=pzsvN3fuBA0 ¡¡IMPORTANTE!!: El WSL debe ser cambiado a version 2 o el proceso de empaquetamiento no funcionará. Esto no se menciona en el tutorial. Para cambiar WSL1 a WSL2, usa el comando `wsl --set-v ubuntu 2` en Windows cmd. Mas info aquí: https://www.youtube.com/watch?v=JBwgsIWUMZQ

- Python instalado también en el WSL2: `sudo apt install python3`

- Kivy instalado también en el WSL2:`sudo apt install -y python3-pip python3-setuptools python3-dev libgles2-mesa-dev libgl1-mesa-dev libgstreamer1.0-dev git-core ffmpeg libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev zlib1g-dev` y después `pip3 install kivy`

- Buildozer instalado en el WSL2 (herramienta para empaquetar la app en formato APK o AAB). INSTALA BUILDOZER: https://buildozer.readthedocs.io/en/latest/installation.html TUTORIAL SOBRE USAR BUILDOZER: https://www.youtube.com/watch?v=pzsvN3fuBA0


CONSIDERACIONES EN EL MOMENTO DE ESCRIBIR LA FICCIÓN EN AUTOROL:

- La ficción puede contener variables de cualquier valor numérico, pero las comparaciones serán siempre de igualdad. El código no entiende comparaciones tipo "si x < 3" o "si x > 3".

- El texto de la ficción puede estar centrado o alienado a la izquierda. En caso de querer cambiar el alineamiento dentro de una misma escena, debe usarse una caja de texto nueva.

- Los enlaces deben estar situados siempre al final de la escena. Pueden incluirse, o no, en una caja que contenga texto, pero ésta debe estar siempre abajo del todo.

- Se pueden incluir condiciones o consecuencias tanto en el texto como en los enlaces.

- Se puede usar negrita, cursiva y subrayado.

- Las imágenes deben añadirse en una caja de texto independiente que no contenga nada más.

- No se pueden utilizar tiradas de dados.

- No utilizar frames ni nada fancy.

- No es necesario incluir un botón "Volver a empezar" en las escenas de muerte. Éste se incluye automáticamente.

- La ficción debe exportarse formato `.json` desde Autorol 3.0.


CONSIDERACIONES EN EL MOMENTO DE CREAR LA APP:

- Echa un vistazo al archivo `main.py` ya que contiene comentarios que indican los pequeños cambios que hay que hacer para adaptarlo a tu ficción.

- Nombra el archivo `.kv` con el nombre de tu app en minuscula. Ejemplo: `miapp.kv`. Usa ese mismo nombre dónde se requiera dentro del archivo `main.py` 

- El archivo `.kv` contiene instrucciones referentes al formato de la app. Después de ver el tutorial de Kivy puedes trastear en él para customizarla.


PARA EMPAQUETARLA:

- El archivo `.json` debe incluirse en el mismo directorio que contiene el archivo `main.py`

- El archivo `autorol.utils` debe incluirse en el mismo directorio que contiene el archivo `main.py`

- El archivo `.kv` debe incluirse en el mismo directorio que contiene el archivo `main.py`.

- En caso de usar varias fuentes, éstas deben guardarse en formato `.ttf` en un directorio llamado `fonts` dentro del directorio que contiene el archivo `main.py`.
  
- En caso de usar imágenes, éstas deben guardarse en formato `.png` o `.jpg` en un directorio llamado `pics` dentro del directorio que contiene el archivo `main.py`.


CUALQUIER DUDA O ERROR: pol.alonso@gmail.com

Disfrutad!






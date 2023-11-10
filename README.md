Miniblog es una aplicación de blog básica construida con Django por los Alumnos Reviglio, Schwartz y Lozano.

Caracteristicas:
- Registro y gestión de usuarios
- Creación, edición y eliminación de posts
- Gestión de categorías
- Agregar y ver comentarios en los posts

Instalacion:
1. Clona este repositorio en tu máquina local.
2. Crea un entorno virtual: `python3 -m venv venv`
3. Activa el entorno virtual: `source venv/bin/activate`
4. Instala las dependencias: `pip install -r requirements.txt`
5. Realiza las migraciones de la base de datos: `python manage.py migrate`

Inicializacion:
1. Inicia el servidor de desarrollo: `python manage.py runserver`
2. Accede a la aplicación en tu navegador: `http://127.0.0.1:8000/home`

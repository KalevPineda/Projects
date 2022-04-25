### Generador de contraseñas con python y django
Existe una pagina principal la cual se encarga de pedir al usuario los requerimeintos necesarios para generar una
contraseña segura, como son:
* Mayusculas
* Caracteres especiales
* Números
Una vez el usuario selecciono las caracteristicas que desea que contenga su contraseña los datos se envian para
procesarlos y retorna una contraseña. Puede recargar la pagina donde se muestra la contrasña para generar Una
nueva.

#### Para ejecutar el proyecto
1. Descarga el codigo del proyecto
2. Crea un entorno virtual **venv** (para este .md se utilizara linux)
```
python3 venv venv

```
3. Ejecuta el entorno vittual **venv**
```
source venv/bin/activate
```
4. Instala django
```
pip install django
```
5. Ejecuta el proyectp
```
python manage.py runserver
```

Esto es todo lo que se tiene que hace para probar el proyecto.

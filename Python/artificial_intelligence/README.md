#### Proyectos
![](https://github.com/KalevPineda/Projects/blob/main/Python/artificial_intelligence/face_access_control/reco.png)
1. **face_access_control**
    - Permite indenticar rostros de que cargan inicialmente en el sistema, este sistema es una prueba de aplicación, puede ser extendido, pero no esta preparado para producción.
    
    - El sistema carga las imagenes de los usarios previamente capturados,despues procede a capturar una foto con la camara, esta imagen es leida, se reduce su tamaño para optimizar el procesamiento de la imagen. El siguiente paso es obtener los encodings de la imagen y se pasa como argumento a una funcion llamada face_recognition.comprare_faces() dentro de el se compara con todas la imagenes cargadas previamente en el sistema.
    
    - En caso de que la imagen ecuentra encuentra al usuario dentro del sistema, manda un mensaje de permitir acceso y muestra un rectangulo verde dentro del recuadro de captura, en caso contrario se muestra un rectangulo rojo y se niega el acceso.

#### Instalación

**Preparar el entorno virtual**
```
python -m venv venv
source venv/bin/activate
pip install face_recognition
pip install opencv_python
```
**Correr el proyecto**
```
python main.py
```

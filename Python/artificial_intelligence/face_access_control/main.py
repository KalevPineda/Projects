

import cv2
import face_recognition


######################################################################################################################
#                                                  UPLOAD DATA USER
######################################################################################################################


#Cargar la imagen de ejemplo con nuestro rostro:
imagen_personal = face_recognition.load_image_file("img/kalev.jpg")
user2 = face_recognition.load_image_file("img/rosario.jpg")
#Extraer los 'encodings' que caracterizan nuestro rostro:
personal_encodings = face_recognition.face_encodings(imagen_personal)[0]
encoding_user2 = face_recognition.face_encodings(user2)[0]
#Definir un array con los encodings y nuestro nombre:
encodings_known = [
    personal_encodings,
    encoding_user2
]
nombres_conocidos = [
    "Kalev Pineda",
    "Rosario Itamar"
]
# NOTA: Como solo queremos identificarnos a nosotros mismos, en realidad no sería necesario definir un array.
# Lo he hecho así para imitar la estructura del código del ejemplo anterior, y para que sea fácil añadir
# nuevos rostros (vuestra pareja o hijos, por ejemplo).

######################################################################################################################
#                                               FUNCTION MAIN
######################################################################################################################


def main():
    #Iniciar la webcam:
    webcam = cv2.VideoCapture(0)
    # NOTA: Si no funciona puedes cambiar el índice '0' por otro, o cambiarlo por la dirección de tu webcam.
    #Cargar una fuente de texto:
    font = cv2.FONT_HERSHEY_COMPLEX
    # Identificar rostros es un proceso costoso. Para poder hacerlo en tiempo real sin que haya retardo
    # vamos a reducir el tamaño de la imagen de la webcam. Esta variable 'reduccion' indica cuanto se va a reducir:
    reduccion = 5 #Con un 5, la imagen se reducirá a 1/5 del tamaño original
    #Recordamos al usuario cuál es la tecla para salir:
    print("\nRecordatorio: pulsa 'ESC' para cerrar.\n")

    while 1:
        #Definimos algunos arrays y variables:
        location_faces = [] #Localizacion de los rostros en la imagen
        encodings_faces = [] #Encodings de los rostros
        nombres_rostros = [] #Nombre de la persona de cada rostro
        nombre = "" #Variable para almacenar el nombre
        #Capturamos una imagen con la webcam:
        valido, img = webcam.read()
        #Si la imagen es válida (es decir, si se ha capturado correctamente), continuamos:
        if valido:
            #La imagen está en el espacio de color BGR, habitual de OpenCV. Hay que convertirla a RGB:
            img_rgb = img[:, :, ::-1]
            #Reducimos el tamaño de la imagen para que sea más rápida de procesar:
            img_rgb = cv2.resize(img_rgb, (0, 0), fx=1.0/reduccion, fy=1.0/reduccion)
            #Localizamos cada rostro de la imagen y extraemos sus encodings:
            location_faces = face_recognition.face_locations(img_rgb)
            encodings_faces = face_recognition.face_encodings(img_rgb, location_faces)
            #Recorremos el array de encodings que hemos encontrado:
            for encoding in encodings_faces:
                #Buscamos si hay alguna coincidencia con algún encoding conocido:
                coincidencias = face_recognition.compare_faces(encodings_known, encoding)
                #El array 'coincidencias' es ahora un array de booleanos. Si contiene algun 'True', es que ha habido alguna coincidencia:
                if True in coincidencias:
                    nombre = nombres_conocidos[coincidencias.index(True)]
                #Si no hay ningún 'True' en el array 'coincidencias', no se ha podido identificar el rostro:
                else:
                    nombre = "???"
                #Añadir el nombre de la persona identificada en el array de nombres:
                nombres_rostros.append(nombre)
            #Dibujamos un recuadro rojo alrededor de los rostros desconocidos, y uno verde alrededor de los conocidos:
            for (top, right, bottom, left), nombre in zip(location_faces, nombres_rostros):
                #Deshacemos la reducción de tamaño para tener las coordenadas de la imagen original:
                top = top*reduccion
                right = right*reduccion
                bottom = bottom*reduccion
                left = left*reduccion
                #Cambiar de color según si se ha identificado el rostro:
                if nombre != "???":
                    color = (0,255,0)
                    print(f"Acceso Aprobado para {nombre}")
                else:
                    color = (0,0,255)
                    print(f"Acceso Denegado")
                #Dibujar un rectángulo alrededor de cada rostro identificado, y escribir el nombre:
                cv2.rectangle(img, (left, top), (right, bottom), color, 2)
                cv2.rectangle(img, (left, bottom - 20), (right, bottom), color, -1)
                cv2.putText(img, nombre, (left, bottom - 6), font, 0.6, (0,0,0), 1)
            #Mostrar el resultado en una ventana:
            cv2.imshow('Output', img)
            #Salir con 'ESC'
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                cv2.destroyAllWindows()
                break
    webcam.release()

######################################################################################################################
#                                                   ENTER POINT
######################################################################################################################

if __name__ =='__main__':
    main()


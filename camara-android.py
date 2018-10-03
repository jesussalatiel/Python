import urllib.request
import cv2
import numpy as np
import imutils

#Busqueda del servidor de la camara ip "shot" es un parametro que necesita la aplicacion IP WebCam en Android
url='http://192.168.0.18:8080/shot.jpg'
#Modelo para la deteccion de rostros
modelo_face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')

while True:
    #Obtenemos la imagen de la camara
    stream = urllib.request.urlopen(url).read()
    #Convertimos la imagen en un array
    img = np.array(bytearray(stream), dtype=np.uint8)
    #Decodificamos la imagen en un formato que OpenCv pueda tratar para el análisis
    img2 = cv2.imdecode(img, -1)
    #Redimencionamos el tamaño de la imagen
    frame = imutils.resize(img2, width=800)
    #Convertimos a escala de grises el frame para el tratamiento de OpenCv
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Hacemos el proceso de deteccion de rostros.
    cara = modelo_face.detectMultiScale(gray, 1.1, 5)
    for(x,y,w,h) in cara:        
        #Dibujamos un cuadro en caso de que se encontrara un rostro en la imagen
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 

    cv2.imshow('Deteccion de Rostros por Ip',frame)
    #Evento que espera que se presionado la letra 'q' para salir del ciclo
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
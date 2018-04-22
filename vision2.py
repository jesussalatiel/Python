import cv2 #Vamos a utilizar la libreria para imagenes
import sys #Interaccion con el sistema

imagen = cv2.imread('srt.jpg') # Leemos la imagen que queremos mostrar 
cv2.rectangle(imagen,(30,660),(1260,128),(0,255,0),2) # Imagen seguido de las coordenadas en la imagen seguido del dibujo para el rectangulo, color y grosor
cv2.imshow("Esta imagen esta genial", imagen) #Titulo de la ventana y la imagen  que se va mmostrar en ella

key = cv2.waitKey(0) & 0xFF # Activamos la opcion de espera por teclado para esperar que presione una tecla

if key==ord("q"): # Comparamos que la letra presionada sea q para poder salir del visor
	cv2.imwrite("srt_salida.png",imagen) #Guardamos una opia de la imagen con distinto nombre 
	cv2.destoyAllWindows()	#Destruimos el proceso de la ventana


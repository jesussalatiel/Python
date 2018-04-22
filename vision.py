import cv2 #Vamos a utilizar la libreria para imagenes
import sys #Interaccion con el sistema

imagen = cv2.imread('srt.jpg') # Leemos la imagen que queremos mostrar 
cv2.putText(imagen,"SUPERCHARGED",(140,280),cv2.FONT_HERSHEY_SIMPLEX,4,(130,255,250),4,cv2.LINE_AA) # Escribimos texto en la imagen especificando imagen, titulo,posicion (x,y), tipo de letra , color de texto, parametros propios del sistema
cv2.putText(imagen,"JESUS SALATIEL",(140,640),cv2.FONT_HERSHEY_SIMPLEX,4,(230, 255, 128),4,cv2.LINE_AA) # Escribimos texto en la imagen especificando imagen, titulo,posicion (x,y), tipo de letra , color de texto, parametros propios del sistema

cv2.imshow("Esta imagen esta genial", imagen) #Titulo de la ventana y la imagen  que se va mmostrar en ella

key = cv2.waitKey(0) & 0xFF # Activamos la opcion de espera por teclado para esperar que presione una tecla

if key==ord("q"): # Comparamos que la letra presionada sea q para poder salir del visor
	cv2.imwrite("srt_salida.png",imagen) #Guardamos una opia de la imagen con distinto nombre 
	cv2.destoyAllWindows()	#Destruimos el proceso de la ventana


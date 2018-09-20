
import pygame  # Libreria que proporciona metodos para juegos
import pygame.midi #Libreria para la reproduccion de sonidos
import time
from pygame.locals import *
from math import *
from random import random 
import sys
import random

"""Tamaño de la pantalla"""
sizeWidth = 1700
sizeHeight = 800


def updateDisplay(screen, balls):
    screen.fill((0, 0, 0))  # Definimos el repaint.
    x = 0 #random.randint(0, 255) 
    y = 255 #random.randint(0, 255) 
    z = 0 #random.randint(0, 255) 
    for ball in balls:  # Recorremos la lista para obtener su propiedades
        """pygame.draw.circle(screen, color, pos, radius, width)"""        
        pygame.draw.circle(screen, (x, y, z), (int(
            ball[1][0]), int(ball[1][1])), int(ball[0]))
    pygame.display.flip()  # Dibujamos en pantalla


def detectColission(balls):
    # Definimos las variables de tipo lista para detectar colision entre los ejes x o y
    tmpBalls = list()
    collision = list()
    for ball_one in range(len(balls)):
        tmpBalls.append(ball_one)
        for ball_two in range(len(balls)):
            if ball_two not in tmpBalls:  # Verificamos que las bolas se tocan algun punto de la cicuferencia
                if hypot((balls[ball_two][1][0]-balls[ball_one][1][0]), (balls[ball_one][1][1]-balls[ball_two][1][1])) < (balls[ball_one][0] + balls[ball_two][0]):
                    collision.append([balls[ball_one], balls[ball_two]])                    
    return collision


def collitionBalls(ball_one, ball_two):
    #Verificamos el area de cada esfera para detectar las colisiones
    if ball_two[1][0] - ball_one[1][0] == 0:
        area = pi / 2.0
    else:
        area = atan((ball_one[1][1]-ball_two[1][1]) /
                    (ball_two[1][0]-ball_one[1][0]))

    v1r = ball_one[2][0]*cos(-area)-(ball_one[2][1])*sin(-area)
    v1s = ball_one[2][0]*sin(-area)+(ball_one[2][1])*cos(-area)
    v2r = ball_two[2][0]*cos(-area)-(ball_two[2][1])*sin(-area)
    v2s = ball_two[2][0]*sin(-area)+(ball_two[2][1])*cos(-area)
    v1r, v2r = v2r, v1r
    ball_one[2][0] = v1r*cos(area)-v1s*sin(area)
    ball_one[2][1] = (v1r*sin(area))+(v1s*cos(area))
    ball_two[2][0] = v2r*cos(area)-v2s*sin(area)
    ball_two[2][1] = (v2r*sin(area))+(v2s*cos(area))


def updatePosition(balls):
    # Si las bolas chocaron se regresan o decrementan en sus coordenadas
    for ball in balls:
        ball[1][0] += ball[2][0]
        ball[1][1] -= ball[2][1]


def limitsFrame(screen, balls):
    #Establecemos los limites de en funcion a los eje y,x de cada esfera
    for bola in balls:
        if bola[1][0]-bola[0] < 0 and bola[2][0] < 0:
            bola[2][0] = -bola[2][0]
        elif bola[1][0]+bola[0] > sizeWidth and bola[2][0] > 0:
            bola[2][0] = -bola[2][0]
        if bola[1][1]-bola[0] < 0 and bola[2][1] > 0:
            bola[2][1] = -bola[2][1]
        elif bola[1][1]+bola[0] > sizeHeight and bola[2][1] < 0:
            bola[2][1] = -bola[2][1]

def generateSound(player):  
    player.set_instrument(9) #Seleccionamos el instrumento
    x = random.randint(50, 90)   
    player.note_on(x, 120) #Activamos la nota (tono, frecuencia)
    time.sleep(0.01) #Esperamos que se reprodusca el sonido
    player.note_off(x, 120)

def main(numBallStart):
    pygame.init()  # Iniciamos pygame
    pygame.midi.init() #Iniciamos midi
    player = pygame.midi.Output(0) #Seleccionamos el dispositivo de salida
    
    # Definimos tamaño de pantalla
    screen = pygame.display.set_mode((sizeWidth, sizeHeight))
    # Establecemos titulo a la pantalla
    pygame.display.set_caption("Generador músical") #Titulo en la pantalla
    """
    Formato para ingresar las pelotas
     balls.append([Radio,[Posicion X, POsicion Y],[Velocidad X, Velocidad Y]])
    """
    balls = list()  # Generamos una lista
   
    for i in range(numBallStart): 
        radio = random.randint(10, 105) 
        rechazo = random.uniform(0.3,1.8)
        balls.append([radio, [radio+(i*100), radio+(i*400)], [rechazo, rechazo]])

    clock = pygame.time.Clock()  # Inicamos proceso para actulizar el pintado de las pelotas
    while(True):  # Ciclo inifinito para seguir la ejecucion del programa

        clock.tick(300)  # Determinamos la velocidad de actualizacion del repaint
        # Ingresamos el objeto para dibujar y la lista de balls
        updateDisplay(screen, balls)
        collision = detectColission(balls)
        for collition in collision:
            collitionBalls(collition[0], collition[1]) #Verifica que exista collision
            generateSound(player) #Generamos un sonido en caso verdadero    

        updatePosition(balls)
        limitsFrame(screen, balls) 

        for event in pygame.event.get():  # Busqueda de eventos para cerrar la pantalla
            if event.type == pygame.QUIT:  # Si es presionado salir
                sys.exit()  # Eliminamos el proceso
    #Variables para limpiar memoria
    del player
    pygame.midi.quit()
    pygame.quit()

if __name__ == '__main__':  # Instancia principal para la ejecucion

    main(2)  # Llamamos al metodo main para iniciar el programa con el parametro n que son 
    #los numeros de bolas a rebotar

#Librerias importadas
import pygame
import numpy as np
import time

pygame.init()
#parametros de la pantalla + inicio de esta
width=750
height=750
pantalla = pygame.display.set_mode((height,width))
#color de fondo
bgcolor=102,204,0
pantalla.fill(bgcolor)
#Cuantas celdas queremos
nhc=25
nvc=25
#Tamaño de la celda
dimcw = width / nhc
dimch = height / nvc
#Celdas Vivas=1 Muertas=0
estadojuego = np.zeros((nhc, nvc))

#Inicio en rango random
estadojuego=np.random.choice([0,1], size=(nhc,nvc))

#Ejecutar codigo
ini=True
while ini:  
    #Copiamos el estado del juego, para usarlo sin modificarlo
    estadojuego_nuevo=np.copy(estadojuego)

    pantalla.fill(bgcolor)
    time.sleep(0.1)
    
    #Configuracion de cada una de las celdas
    for y in range(0,nhc):
        for x in range (0, nvc):

            #Calculamos las celdas cercanas
            #El % hace que (como en el pacman) si sobrepasas el talbero, salga por el otro lado
            vecinos = estadojuego[(x-1) %nhc,(y-1)%nvc] + \
                      estadojuego[(x)%nhc,(y-1)%nvc] + \
                      estadojuego[(x+1)%nhc,(y-1)%nvc] + \
                      estadojuego[(x-1)%nhc,(y)%nvc] + \
                      estadojuego[(x+1)%nhc,(y)%nvc] + \
                      estadojuego[(x-1)%nhc,(y+1)%nvc] + \
                      estadojuego[(x)%nhc,(y+1)%nvc] + \
                      estadojuego[(x+1)%nhc,(y+1)%nvc]
            
            #Excatamente 3 vecinos vivos = revivir
            if estadojuego[x,y] == 0 and vecinos == 3:
                #Revive
                estadojuego_nuevo[x, y] =1
            
            #- 2 o + 3 vecinos = Muerte
            elif estadojuego[x,y] == 1 and (vecinos<2 or vecinos>3):
                #Muere
                estadojuego_nuevo[x, y] =0

            #Coordenadas de las celdas
            poly = [((x) * dimcw, y * dimch),
                    ((x+1) * dimcw, y * dimch),
                    ((x+1) * dimcw, (y+1) * dimch),
                    ((x) * dimcw, (y+1) * dimch)]
            if estadojuego_nuevo[x,y]==0:
                pygame.draw.polygon(pantalla, (102,255,0), poly, 1)
            else:
                pygame.draw.polygon(pantalla, (102,0,102), poly, 0)

    estadojuego=np.copy(estadojuego_nuevo)

    pygame.display.flip()
    #Cerrar ventana
    for cerrar in pygame.event.get():
        if cerrar.type==pygame.QUIT:
            ini=False
pygame.quit()

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
bgcolor=104,217,211
pantalla.fill(bgcolor)
#Cuantas celdas queremos (horizontales y verticales)
celd_horizon=25
vert_horizon=25
#Tamaño de las celdas, segun tamaño de plantilla
dimcw = width / celd_horizon
dimch = height / vert_horizon
#Celdas Vivas=1 Muertas=0
estadojuego = np.zeros((celd_horizon, vert_horizon))

#Inicis el juego en un rango de celdas random
estadojuego=np.random.choice([0,1], size=(celd_horizon,vert_horizon))

#Ejecutar codigo
#Entramos al bucle con ini True y saldremos cuando ini = False
ini=True
while ini:  
    #Copiamos el estado del juego, para usarlo sin modificarlo
    estadojuego_nuevo=np.copy(estadojuego)
    #Configuramos que las celdas pintadas, vuelvan al color de fondo, al cabo de 0.1s
    pantalla.fill(bgcolor)
    time.sleep(0.2)
    
    #Configuracion de cada una de las celdas
    for y in range(0,celd_horizon):
        for x in range (0, vert_horizon):

            #Calculamos las celdas cercanas
            #El % hace que (como en el pacman) si sobrepasas el talbero, salga por el otro lado paralelo
            vecinos = estadojuego[(x-1) %celd_horizon,(y-1)%vert_horizon] + \
                      estadojuego[(x)%celd_horizon,(y-1)%vert_horizon] + \
                      estadojuego[(x+1)%celd_horizon,(y-1)%vert_horizon] + \
                      estadojuego[(x-1)%celd_horizon,(y)%vert_horizon] + \
                      estadojuego[(x+1)%celd_horizon,(y)%vert_horizon] + \
                      estadojuego[(x-1)%celd_horizon,(y+1)%vert_horizon] + \
                      estadojuego[(x)%celd_horizon,(y+1)%vert_horizon] + \
                      estadojuego[(x+1)%celd_horizon,(y+1)%vert_horizon]
            
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
            #Colores y margenes de las celdas
            if estadojuego_nuevo[x,y]==0:
                pygame.draw.polygon(pantalla, (113,174,171), poly, 5)
            else:
                pygame.draw.polygon(pantalla, (208,127,104), poly)
                
    #Copiamos todo el estado de "estadojuego_nuevo" a "estadojuego"
    estadojuego=np.copy(estadojuego_nuevo)

    pygame.display.flip()
    #Cerrar ventana
    for cerrar in pygame.event.get():
        if cerrar.type==pygame.QUIT:
            ini=False
pygame.quit()

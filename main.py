import pygame
import time
from Celda import Celda

# Configuración de la ventanana en pygame

RES = (800, 800)
ANCHO = 800
ALTO = 800
CUADRO = 40
start = False
found = False
path = None

col, filas = ANCHO // CUADRO, ALTO // CUADRO   

pygame.init()
ventana = pygame.display.set_mode(RES)
pygame.display.set_caption("Algoritmos")
reloj = pygame.time.Clock()
font = pygame.font.Font(None, 50)

# Start the timer
start_ticks = None

# Configuración de las Celdas
celdas = [[Celda(i, j) for i in range(col)] for j in range(filas)]

for fila in celdas:
    for celda in fila:
        celda.setVecinos(celdas)

# Configuracion del algoritmo
        
celdas[0][0].inicial = True
celdas[0][0].distancia = 0
priority_queue = [celdas[0][0]]


while True:
    ventana.fill(pygame.Color("black"))

    # checar por eventos en la pantalla
    for event in pygame.event.get():
        # checa si el usuario cierra la ventana
        if event.type == pygame.QUIT:
            exit()
        # obtiene la posición en x, y
        if event.type == pygame.MOUSEBUTTONDOWN and not start:
            click_position = event.pos
            x, y = click_position
            x, y = x // CUADRO, y // CUADRO

            if event.button == 1:           
                celdas[y][x].muro = True

            if event.button == 3 and not start:
                celdas[y][x].target = True
                start = True
                start_ticks = pygame.time.get_ticks()

    # dibujar cada refrescada 
    for fila in celdas:
        for celda in fila:
            celda.dibujarme(ventana, CUADRO)
    
    if start and not found:

        if priority_queue:
            priority_queue.sort(key=lambda x: x.distancia)
            current = priority_queue.pop(0)
            current.visited = True

            if current.target:
                path = current
                found = True

            for vecino in current.vecinos:
                if not vecino.visited and not vecino.muro:
                    distancia_nueva = current.distancia + 1
                    if distancia_nueva < vecino.distancia:
                        vecino.previo = current
                        vecino.distancia = distancia_nueva
                        priority_queue.append(vecino)
                        vecino.frontera = True
            
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        timer_text = font.render(str(seconds), True, pygame.Color("green"))
        ventana.blit(timer_text, (700, 100)) 


    if found and path:
        path.path = True
        path = path.previo
    
    if not priority_queue and not found:
        text = font.render("No solution to the path!", True, pygame.Color("red"))
        text_rect = text.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(text, text_rect)
    


    pygame.display.flip()
    reloj.tick(10)
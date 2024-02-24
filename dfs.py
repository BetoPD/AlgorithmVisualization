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
pygame.display.set_caption("DFS")
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
stack = []
stack.append(celdas[0][0])


while True:
    ventana.fill(pygame.Color("black"))

    mouse_buttons = pygame.mouse.get_pressed()

    if mouse_buttons[0] and not start:
        x, y = pygame.mouse.get_pos()
        x, y = x // CUADRO, y // CUADRO
        celdas[y][x].muro = True

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

            if event.button == 3 and not start:
                celdas[y][x].target = True
                start = True
                start_ticks = pygame.time.get_ticks()

    # dibujar cada refrescada 
    for fila in celdas:
        for celda in fila:
            celda.dibujarme(ventana, CUADRO)
    
    if start and not found:

        if stack:
            current = stack.pop()
            current.visited = True

            if current.target:
                path = current
                found = True

            for neighbor in current.vecinos:
                if not neighbor.visited and not neighbor.muro:
                    stack.append(neighbor)
                    neighbor.previo = current
                    neighbor.frontera = True
        
        seconds = (pygame.time.get_ticks() - start_ticks) // 1000
        timer_text = font.render(str(seconds), True, pygame.Color("green"))
        ventana.blit(timer_text, (700, 100)) 


    if found and path:
        path.path = True
        path = path.previo
    
    if not stack and not found:
        text = font.render("Sin Solución flaco!", True, pygame.Color("red"))
        text_rect = text.get_rect(center=(ANCHO // 2, ALTO // 2))
        ventana.blit(text, text_rect)
    


    pygame.display.flip()
    reloj.tick(60)
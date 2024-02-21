import pygame
import numpy as np

DIAGONAL = False
class Celda:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = False
        self.muro = False
        self.target = False
        self.inicial = False
        self.previo = None
        self.frontera = False
        self.visited = False
        self.distancia = np.Infinity
        self.vecinos = []

    def dibujarme(self, ventana, cuadro):
        # Posición de inicio del dibujo
        x = self.x * cuadro
        y = self.y * cuadro 

        if self.path:
            pygame.draw.rect(ventana, pygame.Color('white'), (x, y, cuadro - 2, cuadro - 2 ))
        elif self.target:
            pygame.draw.rect(ventana, pygame.Color('yellow'), (x, y, cuadro - 2, cuadro - 2 ))
        elif self.inicial:
            pygame.draw.rect(ventana, pygame.Color('orange'), (x, y, cuadro - 2, cuadro - 2 ))
        elif self.visited:
            pygame.draw.rect(ventana, pygame.Color('purple'), (x, y, cuadro - 2, cuadro - 2 ))
        elif self.frontera:
            pygame.draw.rect(ventana, pygame.Color('red'), (x, y, cuadro - 2, cuadro - 2 ))
        elif self.muro:
            pygame.draw.rect(ventana, pygame.Color('black'), (x, y, cuadro - 2, cuadro - 2 ))
        else:
            pygame.draw.rect(ventana, pygame.Color('blue'), (x, y, cuadro - 2, cuadro - 2))
    
    def setVecinos(self, celdas):
        if self.x > 0:
            self.vecinos.append(celdas[self.y][self.x - 1])
        if self.x < len(celdas) - 1:
            self.vecinos.append(celdas[self.y][self.x + 1])
        if self.y > 0:
            self.vecinos.append(celdas[self.y - 1][self.x])
        if self.y < len(celdas) - 1:
            self.vecinos.append(celdas[self.y + 1][self.x])

        if DIAGONAL:
            if self.x > 0 and self.y > 0:
                self.vecinos.append(celdas[self.y - 1][self.x - 1])
            if self.x < len(celdas) - 1 and self.y > 0:
                self.vecinos.append(celdas[self.y - 1][self.x + 1])
            if self.x > 0 and self.y < len(celdas) - 1:
                self.vecinos.append(celdas[self.y + 1][self.x - 1])
            if self.x < len(celdas) - 1 and self.y < len(celdas) - 1:
                self.vecinos.append(celdas[self.y + 1][self.x + 1])
        



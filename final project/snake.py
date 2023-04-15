import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 0
    width = 0

    def _init_(self, start, x_dir=1, y_dir=0, color=(255, 0, 0)):
        pass
    
    def move(self, x_dir, y_dir):
        pass
    
    def draw(self, surface):
        pass
    
class snake(object):
    
    def _init_(self, color, pos):
        pass
    
    def move(self):
        pass
    
    def reset(self, pos):
        pass
    
    def addCube(self):
       pass
    
    def draw(self, surface):
        pass
    
def drawGrid(width, rows, surface):
    size = width // rows
    x = 0
    y = 0
    for l in range(rows):
        x += size
        y += size
        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, width))
        pygame.draw.line(surface, (255, 255, 255), (0, y), (width, y))

def redrawWindow(surface):
    global width, rows
    surface.fill((60, 179, 113))
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSack(rows, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    height = 500
    rows = 20
    window = pygame.display.set_mode((width, height))

    snake = snake((255, 0, 0), (10, 10))

    game_over = False
    clock = pygame.time.Clock()

    while not game_over:
        pygame.time.delay(50)
        # game runs at 10 frams per second
        clock.tick(10)
        redrawWindow(window)
    pass

main()
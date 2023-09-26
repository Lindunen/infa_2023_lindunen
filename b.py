import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

x1 = 100; y1 = 100
x2 = 300; y2 = 200
N = 10
pygame.draw.rect(screen, "#0e9325", (0,200,400,200))
pygame.draw.rect(screen, "#a1eaf5", (0,0,400,200))
pygame.draw.rect(screen, '#936b0e', (70,140,110,90))
pygame.draw.rect(screen, (0,0,0), (70,140,110,90),8)
pygame.draw.polygon(screen,'#eb2f44', [[70,140],[125,50],[180,140]])
pygame.draw.polygon(screen, (0,0,0), [[70,140],[125,50],[180,140]], 2)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.display.update()
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

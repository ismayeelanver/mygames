from math import *
import pygame


pygame.init()

w = 800
h = 800

screen = pygame.display.set_mode((w, h))
testplayer = pygame.Rect(w // 2, h // 2, 10, 10)
delta = 9
while True:
    velocity = testplayer.x / pygame.time.get_ticks()
    screen.fill("White")
    dx = testplayer.x - pygame.mouse.get_pos()[0]
    dy = testplayer.y - pygame.mouse.get_pos()[1]
    ds = (-dx, -dy)
    areax = ds[0] / 2
    areay = ds[1] / 2 
    pygame.draw.line(screen, (0, 0, 0), (areax, areay), pygame.mouse.get_pos())
    pygame.draw.line(screen, (0, 0, 0), (areax, pygame.mouse.get_pos()[1]), pygame.mouse.get_pos())
    pygame.draw.line(screen, (0, 0, 0), (areax, areay), (areax, pygame.mouse.get_pos()[1]))
    pygame.draw.circle(screen, (0, 0, 0), (areax, areay), 10)
    for rn in pygame.event.get():
        if rn.type == pygame.QUIT:
            quit()
    pygame.display.update()

import pygame

pygame.init()

w = 800
h = 800

screen = pygame.display.set_mode((w, h))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
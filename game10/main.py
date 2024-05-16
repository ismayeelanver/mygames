import pygame
from math import *

pygame.init()


w = 800
h = 800
img = "Graphics/"
screen = pygame.display.set_mode((w,h))
jump_speed = 50
speed = 8
delta = 9.00000000000000000003
BG = pygame.image.load(img + "BG.png")


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load(img + "garry.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    def draw(self):
        screen.blit(self.image, self.rect)

class Cloud(pygame.sprite.Sprite):pass

p = Player(w // 2, h // 2)

while True:
    screen.blit(BG, (0, 0))
    p.draw()
    p.rect.y += speed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p.rect.y -= jump_speed
    pygame.display.update()
    pygame.time.Clock().tick(90)
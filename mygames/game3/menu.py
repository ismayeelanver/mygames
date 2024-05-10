# this is the menu for the game

import pygame
from math import sin 

pygame.init()
pygame.display.set_caption("Main Menu")

pygame.mixer.music.load("menu.wav")
pygame.mixer.music.play(-1)
w = 800
h = 800

screen = pygame.display.set_mode((w, h))
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
B = Button(400, 400, pygame.image.load("UI/Button.png"))
B_G = pygame.sprite.Group()
BG = pygame.image.load("Graphics/BG.png")
Play = pygame.font.Font("UI/normal.ttf", 50).render("Play", True, "Black")
logo = pygame.font.Font("UI/normal.ttf", 128).render("Pop 'N Top", True, "Black")
B_G.add(B)
ypos = 100
xpos = 100
while True:
    screen.blit(BG, (0, 0))
    B_G.draw(screen)
    screen.blit(Play, (350, 380))
    screen.blit(logo, (xpos, ypos))
    ypos += sin(pygame.time.get_ticks() / 200)
    xpos += sin(pygame.time.get_ticks() / 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if B.rect.collidepoint(pygame.mouse.get_pos()):
                import main
                pygame.quit()
                exit()
    pygame.display.update()
    pygame.time.Clock().tick(60)

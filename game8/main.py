import pygame
import math

pygame.init()
pygame.display.set_caption("Calling")
pygame.mixer.Channel(0).play(pygame.mixer.Sound("calling.mp3"), loops=-1)
w = 400
h = 800

screen = pygame.display.set_mode((w, h))
BG = pygame.image.load("Graphics/BG.png")
BG1 = pygame.image.load("Graphics/BG1.png")
Accept1 = pygame.image.load("Graphics/button.png")
Accept2 = pygame.image.load("Graphics/button.png")
a1_rect = Accept1.get_rect(center=(80, 600))
a2_rect = Accept2.get_rect(center=(290, 600))
Decline = pygame.image.load("Graphics/button2.png")
d_rect = Decline.get_rect(center=(w // 2, h // 2 + 100))
while True:
    screen.blit(BG, (0, 0))
    screen.blit(Accept1, a1_rect)
    screen.blit(Accept2, a2_rect)
    screen.blit(Decline, d_rect)
    a1_rect.y += math.sin(pygame.time.get_ticks() / 100)
    a2_rect.y += math.sin(pygame.time.get_ticks() / 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if a1_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.display.set_caption("Huggy Wuggy")
                pygame.mixer.Channel(0).stop()
                BG = pygame.image.load("Graphics/BG1.png")
                Accept1.fill((0, 0, 0, 0))
                Accept2.fill((0, 0, 0, 0))
                Decline = pygame.image.load("Graphics/button1.png")
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("attend.mp3"), loops=-1)
            if a2_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.display.set_caption("Huggy Wuggy")
                pygame.mixer.Channel(0).stop()
                BG = pygame.image.load("Graphics/BG1.png")
                Accept1.fill((0, 0, 0, 0))
                Accept2.fill((0, 0, 0, 0))
                Decline = pygame.image.load("Graphics/button1.png")
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("attend.mp3"), loops=-1)
            if d_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.quit()
                quit()
    pygame.display.update()
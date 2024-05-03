import pygame
from math import sin
import random

pygame.init()

pygame.mixer.music.load("main.wav")

pygame.mixer.music.play(-1)

pygame.display.set_caption("Pop 'N Top")
w = 800
h = 800

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Bubble.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/bomb.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

BO = Bomb(400, 100)
B = Bubble(400, 100)
D = pygame.image.load("Graphics/droplets.png")
screen = pygame.display.set_mode((w, h))
BG = pygame.image.load("Graphics/BG.png")
BOG = pygame.sprite.Group()
score = 0
player_speed = 13
bubble_falling_speed = 15
pop = pygame.image.load("Graphics/pop.png")
R = pop.get_rect()
BUG = pygame.sprite.Group()
BUG.add(B)
BOG.add(BO)
while True:
    screen.blit(BG, (0, 0))
    BUG.draw(screen)
    BOG.draw(screen)
    BO.rect.y += 10
    B.rect.y += bubble_falling_speed
    # keep it going down like its floating and going down in the air with a sine wave
    # change x all the time
    B.rect.x += sin(pygame.time.get_ticks() / 90)
    if B.rect.y > h:
        score = 0
        B.rect.y = -100
    
    if BO.rect.y > h:
        BO.rect.x = random.randint(40, 760)
        BO.rect.y = -100
    
    
    
    screen.blit(pygame.font.Font("UI/normal.ttf", 50).render(f"Score: {score}", True, "Black"), (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if B.rect.collidepoint(pygame.mouse.get_pos()):
                B.rect.y = -100
                B.rect.x = random.randint(40, 760)
                screen.blit(D, (B.rect.x, B.rect.y))
                score += 1
                popsound = random.randint(1, 4)
                pygame.mixer.Channel(1).play(pygame.mixer.Sound(f"pop{popsound}.mp3"))
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if BO.rect.collidepoint(pygame.mouse.get_pos()):
                BO.rect.y = -100
                BO.rect.x = random.randint(40, 760)
                screen.blit(pop, pygame.mouse.get_pos())
                score = 0
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("pop.mp3"))
                
        
    pygame.display.update()
    pygame.time.Clock().tick(60)
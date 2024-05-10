import pygame
from math import sin
import random

pygame.init()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("main.wav"), loops=-1)

w = 800
h = 800
screen = pygame.display.set_mode((w, h))
class Container(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Graphics/Container.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Graphics/Ball.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class ExraPointBall(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Graphics/Extra.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

C = Container(400, 700)
E = ExraPointBall(400, 0)
B = Ball(400, 400)
CG = pygame.sprite.Group()
EG = pygame.sprite.Group()
BG_ = pygame.sprite.Group()
BG = pygame.image.load("Graphics/BG.png")
CG.add(C)
EG.add(E)
BG_.add(B)
Score = pygame.image.load("UI/Button.png")
score = 0
while True:
    screen.blit(BG, (0, 0))
    CG.draw(screen)
    BG_.draw(screen)
    EG.draw(screen)
    screen.blit(Score, (340, 10))
    B.rect.x += sin(pygame.time.get_ticks() / 50)
    B.rect.y += 10
    B.rect.y += sin(pygame.time.get_ticks() / 50)
    E.rect.x += sin(pygame.time.get_ticks() / 50)
    E.rect.y += 2
    E.rect.width += sin(pygame.time.get_ticks() / 50)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        C.rect.x -= 10

    if keys[pygame.K_RIGHT]:
        C.rect.x += 10
    
    if C.rect.x < -10:
        C.rect.x = -10
    
    if C.rect.x > 670:
        C.rect.x = 670
    
    if B.rect.y < C.rect.bottom - 40 and B.rect.colliderect(C.rect):
        score += 1
        B.rect.y = -100
        B.rect.x = random.randint(10, 790)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sound/sound.mp3"))
    
    if B.rect.y > h:
        B.rect.y = -100
        B.rect.x = random.randint(10, 790)
        score = 0
    
    if E.rect.y < C.rect.bottom - 40 and E.rect.colliderect(C.rect):
        score += 5
        E.rect.y = -100
        E.rect.x = random.randint(10, 790)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sound/sound.mp3"))
    
    if E.rect.y > h:
        E.rect.y = -100
        E.rect.x = random.randint(10, 790)
    
    Score_text = pygame.font.Font("UI/normal.ttf", 45).render(str(score), True, "White")
    screen.blit(Score_text, (340, 10))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                import menu
    pygame.display.update()
    pygame.time.Clock().tick(60)
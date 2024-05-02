import pygame
from math import sin
import random

pygame.init()

pygame.mixer.music.load("main.wav")

pygame.mixer.music.play(-1)

pygame.display.set_caption("Pop 'N Top")
w = 800
h = 800

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        keys = pygame.key.get_pressed()

class Bubble(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/Bubble.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

B = Bubble(400, 100)
P = Player(400, 700)
D = pygame.image.load("Graphics/droplets.png")
screen = pygame.display.set_mode((w, h))
BG = pygame.image.load("Graphics/BG.png")
score = 0
player_speed = 13
bubble_falling_speed = 5

PG = pygame.sprite.Group()
BUG = pygame.sprite.Group()
BUG.add(B)
PG.add(P)
while True:
    screen.blit(BG, (0, 0))
    BUG.draw(screen)
    PG.draw(screen)
    B.rect.y += bubble_falling_speed
    # keep it going down like its floating and going down in the air with a sine wave
    # change x all the time
    B.rect.x += sin(pygame.time.get_ticks() / 90)
    if B.rect.y > h:
        bubble_falling_speed += 1
        B.rect.y = -100
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        P.rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        P.rect.x += player_speed
    
    if B.rect.colliderect(P.rect):        
        # after a pop there should be droplets coming out of the same image but smaller in a random quantity
        score += 1
        bubble_falling_speed += 1
        screen.blit(D, (B.rect.x, B.rect.y + 40))
        B.rect.y = -100
        B.rect.x = random.randint(40, 760)
        popsound = random.randint(1, 4)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(f"pop{popsound}.mp3"))

    
    if P.rect.x < 0:
        P.rect.x = 0
    
    if P.rect.x > w - 50:
        P.rect.x = w - 50

    screen.blit(pygame.font.Font("UI/normal.ttf", 50).render(f"Score: {score}", True, "Black"), (10, 10))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    pygame.display.update()
    pygame.time.Clock().tick(60)
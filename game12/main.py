import pygame
import random

pygame.init()

size = []
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Ohio's Most Dangerous Game")
pygame.display.set_icon(pygame.image.load("Bullet.png"))

def main():
    pygame.display.update()
    screen.blit(BG, (0, 0))
    PG.draw(screen)
    BU_G.draw(screen)
    player.rect.y += fall_speed
    B.rect.x -= 10
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('jump.mp3'))
        player.rect.y -= player_speed
    
    
   
   

pygame.mixer.music.load("BG.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]


BU_G = pygame.sprite.Group()
B = Bullet(700, 500)
PG = pygame.sprite.Group()
BG = pygame.image.load("BG.png")

player = Player(100, 0)
fall_speed = 4
player_speed = 12
score = 0

PG.add(player)
BU_G.add(B)
while True:
    main()
    if B.rect.x < -100:
        B.rect.x = 500
        B.rect.y = random.randint(0, 500)
        score += 1
    
    if player.rect.colliderect(B.rect):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('hit.mp3'))
        score = 0
        B.rect.x = 500
    
    if player.rect.y < 10:
        player.rect.y = 10
    
    if player.rect.y > h:
        player.rect.y = 0
    
    screen.blit(pygame.font.Font(None, 64).render("Score: " + str(score), True, "Black"), (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.time.Clock().tick(60)

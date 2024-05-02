import pygame
import random

pygame.init()
gap = 350
#size
width = 1280
height = 700
#window
screen = pygame.display.set_mode((width, height))
#flappy nerd
pygame.display.set_caption("Flappy Nerd")
# app icon
pygame.display.set_icon(pygame.image.load('player.png'))
# background music
pygame.mixer.music.load("BG.mp3")
pygame.mixer.music.set_volume(100.5)
pygame.mixer.music.play(-1)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Pipe
class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pos):
        super().__init__()
        self.image = pygame.image.load("pipe.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.pos = pos
        if self.pos == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - 100 / 2]
        elif self.pos == -1:
            self.rect.topleft = [x, y - 100 / 2]
# pipe speed
pipe_speed = 10
# Pipe variable
pipe = Pipe(700, 300, -1)
pipe1 = Pipe(700, 100, 1)
# Pipe group
pipe_group = pygame.sprite.Group()
# Add pipe
pipe_group.add(pipe)
pipe_group.add(pipe1)
# Player variable
player = Player(100, height / 2)
# Player group
player_group = pygame.sprite.Group()
# Add player
player_group.add(player)
# BG
BG = pygame.image.load("BG.png")
# score
score = 0
while True:
    # BG
    screen.blit(BG, (0, 0))
    # Player
    player_group.draw(screen)
    # Pipe
    pipe_group.draw(screen)
    # display score
    screen.blit(pygame.font.Font("normal.ttf", 64).render("Score: " + str(score), True, (255, 255, 255)), (0, 0))
    # player go down
    player.rect.y += 5
    # pipe go right
    pipe.rect.x -= pipe_speed
    pipe1.rect.x -= pipe_speed
    if pipe.rect.x < 0:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound("yes.mp3"))
        score += 1
        pipe.rect.x = width
        pipe.rect.y = random.randint(200, 700)
    
    if pipe1.rect.x < 0:
        pipe1.rect.x = width
        pipe1.rect.y = random.randint(-500, 0)
        if pipe1.rect.y < pipe.rect.y:
            pipe.rect.y += gap
        if pipe.rect.y < pipe1.rect.y:
            pipe1.rect.y += gap
    
    if player.rect.colliderect(pipe.rect) or player.rect.colliderect(pipe1.rect):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("hit.mp3"))
        score = 0
    
    if player.rect.y < 0:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("hit.mp3"))
        score = 0
        player.rect.y = height / 2
    
    if player.rect.y > height:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("hit.mp3"))
        score = 0
        player.rect.y = height / 2
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        player.rect.y -= 13
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    pygame.time.Clock().tick(60)
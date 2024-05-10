import pygame


pygame.init()
pygame.mixer.Channel(1).play(pygame.mixer.Sound("game.mp3"), loops=-1)
w = 800
h = 800
font = pygame.font.Font("normal.ttf", 50)
screen = pygame.display.set_mode((w, h))
class Track(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Graphics/track.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def draw(self, surface):
        surface.blit(self.image, self.rect.center)

class Train(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load("Graphics/train.png")
        self.rect = self.image.get_rect()
        self.rect.center = [w, T.rect.y]
    def draw(self, surface):
        surface.blit(self.image, self.rect.center)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load("Graphics/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
    def draw(self, surface):
        surface.blit(self.image, self.rect.center)


T = Track(0, 400)
TR = Train()
P = Player(400, 400)
BG = pygame.image.load("Graphics/BG.png")
B = pygame.image.load("UI/Button.png")
score = 0
while True:
   screen.blit(font.render(str(int(score / 11)), True, "Black"), (w // 2, 0))
   pygame.display.update()
   pygame.time.Clock().tick(60)
   screen.blit(BG, (0, 0))
   T.draw(screen)
   TR.draw(screen)
   P.draw(screen)
   screen.blit(B, (w // 2, 0))
   TR.rect.x -= 10
   TR.rect.y = T.rect.y
   T.rect.y += 10
   
   if T.rect.y > h:
       pygame.mixer.Channel(0).play(pygame.mixer.Sound("train.mp3"))
       T.rect.y = -200
   if TR.rect.x < -300:
       pygame.mixer.Channel(0).play(pygame.mixer.Sound("train.mp3"))
       TR.rect.x = w - 20
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:
       P.rect.x -= 20
   if keys[pygame.K_RIGHT]:
       P.rect.x += 20

   if P.rect.x < 0:
       P.rect.x = 0
   if P.rect.x > w - 40:
       P.rect.x = w - 40
   if P.rect.colliderect(TR.rect) or P.rect.collidepoint(TR.rect.center):
       score = 0

   if P.rect.colliderect(T.rect):
       score += 1
   for rn in pygame.event.get():
        if rn.type == pygame.QUIT:
            exit()

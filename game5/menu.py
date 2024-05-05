import pygame
from math import sin

pygame.init()

w = 800
h = 800
pygame.mixer.Channel(0).play(pygame.mixer.Sound("menu.mp3"), loops=-1)
class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("UI/Button.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

PB = Button(w // 2, h // 2)
QB = Button(w // 2, h // 2 + 100)
BG_ = pygame.sprite.Group()
BG_.add(PB)
BG_.add(QB)
PlayText = pygame.font.Font("normal.ttf", 32).render("Play", True, "Black")
QuitText = pygame.font.Font("normal.ttf", 32).render("Quit", True, "Black")
LogoText = pygame.font.Font("normal.ttf", 64).render("Dont get hit", True, "Black")
screen = pygame.display.set_mode((w, h))
BG = pygame.image.load("Graphics/BG.png")
movex = 0
movey = 200
while True:
    pygame.display.update()
    screen.blit(BG, (0, 0))
    BG_.update()
    BG_.draw(screen)
    screen.blit(PlayText, (w // 2 - 90, h // 2 - 20))
    screen.blit(QuitText, (w // 2 - 90, h // 2 + 80))
    screen.blit(LogoText, (movex, movey))
    movex += sin(pygame.time.get_ticks() / 100)
    movey += sin(pygame.time.get_ticks() / 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if PB.rect.collidepoint(pygame.mouse.get_pos()):
                import main
            elif QB.rect.collidepoint(pygame.mouse.get_pos()):
                quit()
    pygame.time.Clock().tick(60)

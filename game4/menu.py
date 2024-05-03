import pygame

pygame.init()

pygame.mixer.Channel(0).play(pygame.mixer.Sound("menu.wav"), loops=-1)

w = 800
h = 800

screen = pygame.display.set_mode((w, h))

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("UI/Button.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

B = Button(400, 400)
BG = pygame.sprite.Group()

BG.add(B)
Play_text = pygame.font.Font("UI/normal.ttf", 24).render("Play", True, "Black")
while True:
    screen.blit(pygame.image.load("Graphics/BG.png"), (0, 0))
    BG.draw(screen)
    screen.blit(Play_text, (380, 380))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if B.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.mixer.Channel(1).play(pygame.mixer.Sound("Sound/sound.mp3"))
                import main
    pygame.display.update()
    pygame.time.Clock().tick(60)
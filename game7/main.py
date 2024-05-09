import math
import pygame
from settings import *

class Pointer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("Graphics/pointer.png")
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.angle = 0

    def update(self):
        dx = pygame.mouse.get_pos()[0] - WIDTH / 2
        dy = -(pygame.mouse.get_pos()[1] - HEIGHT / 2)
        self.angle = math.degrees(math.atan2(dy, dx))
        self.image = pygame.transform.rotate(self.original_image, self.angle - 90)
        self.rect = self.image.get_rect(center=self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        pygame.draw.line(surface, "orange", self.rect.center, pygame.mouse.get_pos(), 1)

P = Pointer()
while True:
    screen.fill("White")
    pygame.mouse.set_visible(False)
    
    P.update()
    P.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.circle(screen, "orange", pygame.mouse.get_pos(), 10)
    pygame.time.Clock().tick(FPS)
    pygame.display.update()

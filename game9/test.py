import pygame
import math

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 30)
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1]
]

width = 650
height = 450
screen = pygame.display.set_mode((width, height))
foundx, foundy = 0, 0
wall = pygame.Rect(foundx, foundy, 50, 50)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.x = 100
        self.y = 100
        self.angle = 0  # Angle in radians
        self.speed = 5
    def draw(self):
        pygame.draw.circle(screen, "blue", (self.x, self.y), 25)
        # Draw line representing the direction the player is facing
        endx = self.x + math.cos(self.angle) * 50
        endy = self.y + math.sin(self.angle) * 50
        pygame.draw.line(screen, "white", (self.x, self.y), (endx, endy), 2)

p = Player()

while True:
    screen.fill("black")
    p.draw()
    
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == 1:
                foundx, foundy = x * 50, y * 50
                pygame.draw.rect(screen, "grey", (foundx, foundy, 50, 50))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        p.angle += 0.1  # Rotate left
    if keys[pygame.K_d]:
        p.angle -= 0.1  # Rotate right
    if keys[pygame.K_w]:
        p.x += math.cos(p.angle) * p.speed  # Move forward
        p.y -= math.sin(p.angle) * p.speed
    if keys[pygame.K_s]:
        p.x -= math.cos(p.angle) * p.speed  # Move backward
        p.y += math.sin(p.angle) * p.speed
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    pygame.display.update()
    pygame.time.Clock().tick(60)

#!/usr/bin/env python3
import pygame
from math import atan2, sin, cos, degrees
import random

pygame.init()
pygame.mixer.Channel(0).play(pygame.mixer.Sound("song.mp3"), loops=-1)
pygame.display.set_icon(pygame.image.load("Graphics/player.png"))

# init
w = 800
h = 800


class GetFps:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.text = str(int(60))
    
    def update(self):
        self.clock.tick(fps.clock.get_fps())
        pygame.display.set_caption("Shooter2d FPS: " + self.text)

fps = GetFps()
BG = pygame.image.load("Graphics/BG.png")
screen = pygame.display.set_mode((w, h))
player = pygame.image.load("Graphics/player.png").convert_alpha()
player_health = 100
bullets = []
bullet_speed = 100
class Enemy:
    def __init__(self):
        self.image = pygame.image.load("Graphics/enemy.png").convert_alpha()
        self.rect = self.image.get_rect(center=(-100, random.randint(50, h-50)))
        self.speed = 1
        self.health = 200

    def update(self, player_pos):
        dx = player_pos[0] - self.rect.centerx
        dy = player_pos[1] - self.rect.centery
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist != 0:
            self.rect.x += dx * self.speed / dist
            self.rect.y += dy * self.speed / dist
enemy = Enemy()
score = 0
while True:
    boss_bar = pygame.Rect(0, 0, enemy.health, 20)
    player_health_bar = pygame.Rect(w // 2, 0, player_health, 20)
    fps.update()
    screen.blit(BG, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    player_pos = (w // 2, h // 2)
    
    # Calculate angle and direction vector
    x_dist = mouse_pos[0] - player_pos[0]
    y_dist = mouse_pos[1] - player_pos[1]
    angle = atan2(-y_dist, x_dist)
    direction = [cos(angle), -sin(angle)]

    
    # Rotate player image
    player1 = pygame.transform.rotate(player, degrees(angle) - 90)
    player1_rect = player1.get_rect(center=player_pos)
    screen.blit(player1, player1_rect)

    enemy.update(player_pos)
    screen.blit(enemy.image, enemy.rect)
    
    pygame.draw.circle(screen, (255, 0, 0), mouse_pos, 5)
    pygame.mouse.set_visible(False)
    
    for bullet in bullets:
        bullet[0] += direction[0] * bullet_speed
        bullet[1] += direction[1] * bullet_speed
        pygame.draw.circle(screen, (0, 0, 0), (int(bullet[0]), int(bullet[1])), 10)
        if not 0 < bullet[0] < w or not 0 < bullet[1] < h:
            bullets.remove(bullet)
    
    if bullets and enemy.rect.collidepoint(bullets[-1]):
        pygame.mixer.Channel(1).play(pygame.mixer.Sound("kill.mp3"))
        enemy.health -= 20
        bullets.remove(bullet)
        score += 1
    
    pygame.draw.rect(screen, (255, 0, 0), boss_bar)
    pygame.draw.rect(screen, (0, 255, 0), player_health_bar)
    screen.blit(pygame.font.Font(None, 32).render(str(score), True, "Black"), (w - 40, h - 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            bullets.append(list(player_pos))
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("shoot.mp3"))
    
    if enemy.health <= 0:
        pygame.mixer.Channel(3).play(pygame.mixer.Sound("kill.mp3"))
        enemy = Enemy()
    
    if player1_rect.collidepoint(enemy.rect.center):
        player_health -= 10

    if player_health <= 0:
        player_health = 100
        enemy = Enemy()
        pygame.mixer.Channel(4).play(pygame.mixer.Sound("die.mp3"))
    pygame.display.update()
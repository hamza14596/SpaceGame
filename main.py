import pygame
from pygame import mixer
import random
import math
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

pygame.init()
mixer.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Outer Heroes")

background = pygame.image.load(resource_path("bgi.png"))
mixer.music.load(resource_path('AttackOfTheKillerQueen.wav'))
mixer.music.set_volume(0.5)
mixer.music.play(-1)

playerFace = pygame.image.load(resource_path('spaceship.png'))
playerX = 370
playerY = 480
playerX_change = 0

ghostFace = pygame.image.load(resource_path('space.png'))
ghostX = []
ghostY = []
ghostX_change = []
ghostY_change = []
num_of_ghosts = 6

for i in range(num_of_ghosts):
    ghostX.append(random.randint(0, 736))
    ghostY.append(random.randint(50, 150))
    ghostX_change.append(0.3)
    ghostY_change.append(50)

bulletFace = pygame.image.load(resource_path('bullet.png'))
bulletX = playerX
bulletY = 480
bulletY_change = 3
bulletFlag = "Ready"

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
ScoreX = 15
ScoreY = 15

over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerFace, (x, y))

def ghost(x, y):
    screen.blit(ghostFace, (x, y))

def bullet_fire(x, y):
    global bulletFlag
    bulletFlag = "Fire"
    screen.blit(bulletFace, (x + 10, y + 10))

def is_collision(ghostX, ghostY, bulletX, bulletY):
    distance = math.sqrt((math.pow(ghostX - bulletX, 2)) + (math.pow(ghostY - bulletY, 2)))
    return distance < 27

explosion_sound = mixer.Sound(resource_path('deltarune-explosionn.wav'))
explosion_sound.set_volume(0.5)

running = True
game_over = False

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.7
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.7
                if event.key == pygame.K_UP:
                    if bulletFlag == "Ready":
                        bullet_sound = mixer.Sound(resource_path('laser.wav'))
                        bullet_sound.set_volume(0.2)
                        bullet_sound.play()
                        bulletX = playerX
                        bullet_fire(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    if not game_over:
        playerX += playerX_change
        playerX = max(0, min(playerX, 736))

        for i in range(num_of_ghosts):
            if ghostY[i] + 64 >= playerY and ghostY[i] <= playerY + 64 and ghostX[i] < playerX + 64 and ghostX[i] + 64 > playerX:
                for j in range(num_of_ghosts):
                    ghostY[j] = 2000
                game_over = True
                explosion_sound.play()
                break

            ghostX[i] += ghostX_change[i]
            if ghostX[i] >= 736:
                ghostX_change[i] = -0.5
                ghostY[i] += ghostY_change[i]
            elif ghostX[i] <= 0:
                ghostX_change[i] = 0.5
                ghostY[i] += ghostY_change[i]

            collision = is_collision(ghostX[i], ghostY[i], bulletX, bulletY)
            if collision:
                bulletY = 480
                bulletFlag = "Ready"
                score_value += 1
                ghostX[i] = random.randint(0, 736)
                ghostY[i] = random.randint(50, 150)

            ghost(ghostX[i], ghostY[i])

        if bulletY <= 0:
            bulletY = 480
            bulletFlag = "Ready"

        if bulletFlag == "Fire":
            bullet_fire(bulletX, bulletY)
            bulletY -= bulletY_change

        player(playerX, playerY)
        show_score(ScoreX, ScoreY)

    else:
        game_over_text()

    pygame.display.update()

import pygame
import random
import math

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Outer Heroes")
background = pygame.image.load("bgi.png")

playerFace = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

ghostFace = pygame.image.load('space.png')
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

bulletFace = pygame.image.load('bullet.png')
bulletX = playerX
bulletY = 480
bulletY_change = 3
bulletFlag = "Ready"

score = 0

def player(x, y):
    screen.blit(playerFace, (x, y))

def ghost(x, y):
    screen.blit(ghostFace, (x, y))

def bullet_fire(x, y):
    global bulletFlag
    bulletFlag = "Fire"
    screen.blit(bulletFace, (x, y + 10))

def is_collision(ghostX, ghostY, bulletX, bulletY):
    distance = math.sqrt((math.pow(ghostX - bulletX, 2)) + (math.pow(ghostY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_UP:
                if bulletFlag == "Ready":
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_ghosts):
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
            score += 1
            print("Score:", score)
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
    pygame.display.update()

   
    
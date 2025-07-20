import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Outer Heroes")
background = pygame.image.load("bgi.png")

playerFace = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

GhostFace = pygame.image.load('space.png')
GhostX = random.randint (0,736)
GhostY = random.randint (0,200)
GhostX_change = 0.3
GhostY_change = 50   

BulletFace = pygame.image.load('bullet.png')
BulletX = playerX
BulletY = 480
BulletY_change = 3
BulletX_change = 0
BulletFlag = "Ready"
 

def player(x,y):
    screen.blit(playerFace, (x,y))

def Ghost(x,y):
    screen.blit(GhostFace, (x,y))

def Bullet_Fire(x,y):
    global BulletFlag
    BulletFlag = "Fire"
    screen.blit(BulletFace,(x,y+10))



running = True 
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT :
                playerX_change = 0.7     
            if event.key == pygame.K_UP:
                 Bullet_Fire(playerX,BulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change = 0
        

    playerX += playerX_change
    if playerX <=0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736

        
    if GhostX >=736 :
        GhostX_change = -0.5
        GhostY += GhostY_change
    elif GhostX <= 0 :     
        GhostX_change = 0.5
        GhostY += GhostY_change
    GhostX += GhostX_change

    if BulletFlag is "Fire":
        Bullet_Fire(playerX,BulletY)
        BulletY -= BulletY_change

    player(playerX,playerY)
    Ghost(GhostX,GhostY)
    pygame.display.update() 

   
    
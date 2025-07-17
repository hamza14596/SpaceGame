import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Outer Heroes")

playerFace = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480



def player(x,y):
    screen.blit(playerFace, (x,y))

running = True 
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        playerX_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT :
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                playerX_change = 0
       

    playerX += playerX_change
    
    if playerX <=0 :
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX,playerY)
    pygame.display.update()

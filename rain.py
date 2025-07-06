import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))

pygame.display.set_caption("Outer Heroes")

playerFace = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480



def player():
    screen.blit(playerFace, (playerX,playerY))

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    player()
    
    pygame.display.update()
    
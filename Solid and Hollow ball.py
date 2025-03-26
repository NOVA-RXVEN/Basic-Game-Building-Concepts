import pygame

pygame.init()

window = pygame.display.set_mode((500,500))

window.fill((0,0,0))

white = ((255,255,255))

pygame.draw.circle(window, white, (300,300), 50)
pygame.draw.circle(window, white, (100,100), 50, 4)

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
pygame.quit()
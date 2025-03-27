import pygame

pygame.init()
pygame.display.set_caption("Different Shapes")
screen = pygame.display.set_mode((500,500))
screen.fill((165, 165, 165 ))
x = 0

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    pygame.draw.rect(screen, (227, 22, 22), pygame.Rect(40,40, 180, 180))
    pygame.draw.circle(screen, (255, 255, 0), (130,355), 90, 5)
    pygame.draw.circle(screen, (0,0,0), (365,135), 95)
    pygame.draw.circle(screen, (18, 216, 33), (365,135), 95, draw_top_right = True, draw_bottom_left = True)
    
    if pygame.mouse.get_pressed()[0] == True:
        x += 0.001
    elif pygame.mouse.get_pressed()[2] == True:
        x -= 0.001
    pygame.draw.arc(screen, (0, 0, 255), (43,43, 175, 175), 0, x, width = 7)
    
    pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, (0,0,255), (370,355), pos)
    pygame.display.flip()
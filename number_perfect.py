import pygame

pygame.init()

GREY = (150,150,150)
WHITE = (255,255,255)

screen = pygame.display.set_mode((500,600))
running = True
while running :
    screen.fill(GREY)
    #toa do chuot
    mouse_x, mouse_y = pygame.mouse.get_pos()
    print(mouse_x,mouse_y)

    #in ra cac o trong
    pygame.draw.rect(screen,WHITE,(100,100,50,50))
    pygame.draw.rect(screen,WHITE,(300,100,100,50))
    pygame.draw.rect(screen,WHITE,(300,200,100,50))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                print("halo")
            

        
    pygame.display.flip()

pygame.quit() 
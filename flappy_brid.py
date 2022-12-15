import pygame , sys,random
#tao ham cho game
def draw_floor():#ham tao san
    screen.blit(floor,(floor_x_pos,650))
    screen.blit(floor,(floor_x_pos+432,650))
def create_pipe():#ham tao ong
    random_pipi_pos = random.choice(pipe_height)#thay doi chieu cao cot
    bottom_pipe = pipe_surface.get_rect(midtop = (500,random_pipi_pos))
    top_pipe = pipe_surface.get_rect(midtop = (500,random_pipi_pos-690))
    return bottom_pipe , top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 3.5#toc do ong
    return pipes
def draw_pipe(pipes):#ham ve ong
    for pipe in pipes:
        if pipe.bottom >= 768:
            screen.blit(pipe_surface,pipe)
        else:
            flio_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flio_pipe,pipe)

        screen.blit(pipe_surface,pipe)
def check_collision(pipes):
    for pipe in pipes:
          if brid_rect.colliderect(pipe):
            return False

    if brid_rect.top <= 0 or brid_rect.bottom >= 768:
       return False
    return True
def rotate_bird(bird1):
    new_bird = pygame.transform.rotozoom(bird1,-brid_movement*2,1)
    return new_bird
def score_display(game_state):
    if game_state == 'main game':
       score_surface = game_font.render(f'Score:{int(score)}',True,(255,255,255))
       score_rect = score_surface.get_rect(center = (216,100))
       screen.blit(score_surface,score_rect)
    if game_state == 'game_over':
       score_surface = game_font.render(f'Score:{int(score)}',True,(255,255,255))
       score_rect = score_surface.get_rect(center = (216,100))
       screen.blit(score_surface,score_rect)

       hight_score_surface = game_font.render(f'High Score:{int(high_score)}',True,(255,255,255))
       hight_score_rect = hight_score_surface.get_rect(center = (216,610))
       screen.blit(hight_score_surface,hight_score_rect)
def update_store(score,high_score):
    if score > high_score:
        high_score = score
    return high_score
pygame.init()
screen = pygame.display.set_mode((432,768))#kich thuoc cua so
clock= pygame.time.Clock()
game_font = pygame.font.SysFont('consolas',40)
#tao cac bien cho game
gravity = 0.25
brid_movement = 0
game_active = True
score = 0
high_score = 0
#chen background
bg = pygame.image.load('/home/hungbv-debian/Downloads/background2.png').convert()
bg = pygame.transform.scale2x(bg)
#chen san
floor = pygame.image.load('/home/hungbv-debian/Downloads/be1.png').convert()
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#tao chim
brid = pygame.image.load('/home/hungbv-debian/Downloads/brid.png').convert_alpha()
     #brid = pygame.transform.scale2x(brid)
brid_rect = brid.get_rect(center = (100,384))
#tao ong 
pipe_surface = pygame.image.load('/home/hungbv-debian/Downloads/cot.png').convert()
      #pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
#tao timer
spawnpipe = pygame.USEREVENT
pygame.time.set_timer(spawnpipe,1200)
pipe_height = [200,300,400]
#tao man hinh ket thuc
brid = pygame.image.load('/home/hungbv-debian/Downloads/brid.png').convert_alpha()
while True:  
    for event in pygame.event.get():
        #command de dong cua so
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                brid_movement = 0
                brid_movement = -6.9 
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                brid_rect.center = (100,384)
                brid_movement = 0
                score = 0
        if event.type == spawnpipe:
            pipe_list.extend(create_pipe())
            

    screen.blit(bg,(0,0))
    if game_active:
        #chim
        brid_movement += gravity 
        rotated_bird = rotate_bird(brid)
        brid_rect.centery += brid_movement
        screen.blit(rotated_bird,brid_rect) 
        game_active = check_collision(pipe_list) 
        #ong
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        score +=0.0075
        score_display('main game')
    else:
        high_score = update_store(score,high_score)
        score_display('game_over')
    #san 
    floor_x_pos -= 1#toc do san
    draw_floor()
    if floor_x_pos <= -432:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)


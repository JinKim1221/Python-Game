# Frame per second
import pygame
import random
##########################################################################
################# General Initialization that you must do#################
pygame.init() # neccessary initialization

# screen setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Practice")

# FPS
clock = pygame.time.Clock()
##########################################################################

##########################################################################
# 1. user game initialization (background, game images, position, font, font, etc)
# Background
background = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/background.png")

# Character Info
ninja = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/ninja.png")
ninja_size = ninja.get_rect()
ninja_width = ninja_size.width
ninja_height = ninja_size.height
ninja_x_pos = (screen_width / 2) - (ninja_width / 2)
ninja_y_pos = screen_height - ninja_height

# Character Movement
ninja_to_x = 0

ninja_speed = 1

# Enemy Info
poo = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/poo.jpg")
poo_size = poo.get_rect()
poo_width = poo_size[0]
poo_height = poo_size[1]
poo_x_pos = random.randint(0, screen_width - poo_width)
poo_y_pos = 0
poo_speed = 10

# Event loop to prevent closing the window
running = True # game is running
while running:
    delta = clock.tick(30) # set frames per second

    # 2. Dealing with the events such as keyboard, mouse and so on
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False

        if event.type == pygame.KEYDOWN : 
            if event.key == pygame.K_LEFT : 
                ninja_to_x -= ninja_speed
            elif event.key == pygame.K_RIGHT :
                ninja_to_x += ninja_speed

        if event.type == pygame.KEYUP : 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                ninja_to_x = 0
    
    
    # 3. Game character's position
    ninja_x_pos += ninja_to_x * delta

    if ninja_x_pos < 0 : 
        ninja_x_pos = 0
    elif ninja_x_pos > (screen_width - ninja_width) :
        ninja_x_pos = (screen_width - ninja_width)
    
    # 3-1 Game enemy's position
    poo_y_pos += poo_speed
    if poo_y_pos > screen_height :
        poo_y_pos = 0
        poo_x_pos = random.randint(0, screen_width - poo_width)
        
    # 4. Dealing with collision 
    ninja_rect = ninja.get_rect()
    ninja_rect.left = ninja_x_pos
    ninja_rect.top = ninja_y_pos
    
    poo_rect = poo.get_rect()
    poo_rect.left = poo_x_pos
    poo_rect.top = poo_y_pos

    if ninja_rect.colliderect(poo_rect) : 
        running = False

    # 5. Draw on the window
    screen.blit(background,(0,0))
    screen.blit(ninja, (ninja_x_pos, ninja_y_pos))
    screen.blit(poo,(poo_x_pos, poo_y_pos))


    pygame.display.update() # redraw the background


# game finished
pygame.quit()
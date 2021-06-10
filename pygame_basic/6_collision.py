# Frame per second
import pygame

pygame.init() # neccessary initialization

# screen setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# background setting
background = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/background.png")

# character setting
character = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/character.png")
character_size = character.get_rect().size # get the size of image
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2) # position that is a half of the screen
character_y_pos = screen_height - character_height # position that is at the bottom of the screen

# character position to be moved
to_x = 0
to_y = 0

# character speed 
character_speed = 0.6

# FPS
clock = pygame.time.Clock()



######### Enemy #########
enemy = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/enemy.png")
enemy_size = character.get_rect().size # get the size of image
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) # position that is a half of the screen
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) # position that is at the bottom of the screen


# set title
pygame.display.set_caption("Python Game")

# Event loop to prevent closing the window
running = True # game is running
while running:
    delta = clock.tick(60) # set frames per second

    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False
        if event.type == pygame.KEYDOWN: # if key is pressed
            if event.key == pygame.K_LEFT: # move the character to the left
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # move the character to the right
                to_x += character_speed
            elif event.key == pygame.K_UP: # move the character to up
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # move the character to down
                to_y += character_speed
        if event.type ==pygame.KEYUP: # key is unpressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
                

    character_x_pos += to_x * delta
    character_y_pos += to_y * delta
    
    # Horizontal
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    # Vertical
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # character information update for disposal of collision
    character_rect = character.get_rect() # get information of height and width of character
    # character_rect on the window is updated
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    # enemy information update for disposal of collision
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # check collision
    if character_rect.colliderect(enemy_rect):
        print("collision occured")
        running = False

    screen.blit(background, (0,0)) # draw the background
    screen.blit(character, (character_x_pos, character_y_pos)) # draw the character
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos)) # draw the enemy
    pygame.display.update() # redraw the background

# game finished
pygame.quit()
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

# set title
pygame.display.set_caption("Python Game")

# Event loop to prevent closing the window
running = True # game is running
while running:
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False
        if event.type == pygame.KEYDOWN: # if key is pressed
            if event.key == pygame.K_LEFT: # move the character to the left
                to_x -= 5
            elif event.key == pygame.K_RIGHT: # move the character to the right
                to_x += 5
            elif event.key == pygame.K_UP: # move the character to up
                to_y -= 5
            elif event.key == pygame.K_DOWN: # move the character to down
                to_y += 5
        if event.type ==pygame.KEYUP: # key is unpressed
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x =0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y =0
                

    character_x_pos += to_x
    character_y_pos += to_y

    screen.blit(background, (0,0)) # draw the background
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update() # redraw the background

# game finished
pygame.quit()
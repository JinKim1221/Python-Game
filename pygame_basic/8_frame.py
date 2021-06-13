# Frame per second
import pygame
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




# Event loop to prevent closing the window
running = True # game is running
while running:
    delta = clock.tick(30) # set frames per second

    # 2. Dealing with the events such as keyboard, mouse and so on
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False

    # 3. Game character's position

 
    # 4. Dealing with collision 
    

    # 5. Draw on the window

    pygame.display.update() # redraw the background


# game finished
pygame.quit()
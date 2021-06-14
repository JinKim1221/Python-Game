import pygame
import random
import os
##########################################################################
################# General Initialization that you must do#################
pygame.init() # neccessary initialization

# screen setting
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Ballst")

# FPS
clock = pygame.time.Clock()
##########################################################################

##########################################################################
# 1. user game initialization (background, game images, position, font, font, etc)
# Background
current_path = os.path.dirname(__file__) # get the current file path
image_path = os.path.join(current_path, "images") # get the image folder path

background = pygame.image.load(os.path.join(image_path, "background.png"))

stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # the character will be on the stage

# Character Info
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect()
character_width = character_size.width
character_height = character_size.height
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - stage_height - character_height



# Event loop to prevent closing the window
running = True # game is running
while running:
    delta = clock.tick(30) # set frames per second

    # 2. Dealing with the events such as keyboard, mouse and so on
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False


    
    
    # 3. Game character's position

    
    # 3-1 Game enemy's position

    # 4. Dealing with collision 


    # 5. Draw on the window
    screen.blit(background,(0,0))
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))


    pygame.display.update() # redraw the background


# game finished
pygame.quit()
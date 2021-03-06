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

# Movement of character
character_to_x = 0

# Character Speed
character_speed = 5

# Weapon Info
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]

# Weapon can be triggered several times at once
weapons = []

# Weapon Speed
weapon_speed = 10


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
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT :
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE :
                weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        
        if event.type == pygame.KEYUP :
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
                character_to_x = 0

    
    # 3. Game character's position setting
    character_x_pos += character_to_x

    if character_x_pos < 0 : 
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width


    # 3-1 Weapon's position re-setting
    # weapon is moving upwards
    weapons = [ [w[0], w[1] - weapon_speed] for w in  weapons]

    # remove weapons once they reach top
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    # 3-2 Game enemy's position

    # 4. Dealing with collision 


    # 5. Draw on the window
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    

    pygame.display.update() # redraw the background


# game finished
pygame.quit()
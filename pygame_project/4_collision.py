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

# Balls Info
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]

# Balls Speed depending on the size
ball_speed_y = [-18, -15, -12, -9]
 # speed value that assigned to index 0 -> balloon1, 1-> balloon2, 2-> balloon2, 3-> balloon4

# Balls
balls = []

# the biggest ball at first
balls.append({
    "pos_x" : 50,  # x position of the ball
    "pos_y" : 50,  # y position of the ball
    "img_index" : 0, # index of the ball
    "to_x" : 3,    # movement to x, -3 to left, 3 to right
    "to_y" : -6,   # movement to y
    "init_spd_y" : ball_speed_y[0]}) # initial speed for y

# weapon and ball to disappear
weapon_to_remove = -1
ball_to_remove = -1

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

    
    # 3. Character's position setting
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

    # 3-2 Ball's position
    # enumerate(LIST) to get index of list and value
    for ball_index, ball_value in enumerate(balls) : 
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_img_index = ball_value["img_index"]

        ball_size = ball_images[ball_img_index].get_rect().size
        ball_width = ball_size[0]
        ball_height = ball_size[1]

        # left to right or right to left when the ball reached to the wall
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width :
            ball_value["to_x"] =  ball_value["to_x"] * -1 
        
        # Horizontal position
        # when the ball bounced on the stage
        if ball_pos_y >= screen_height - stage_height - ball_height :
            ball_value["to_y"] = ball_value["init_spd_y"]
        else : # Speed decreased after the ball reached the stage to make a curve
            ball_value["to_y"] += 0.5

        ball_value["pos_x"] += ball_value["to_x"]
        ball_value["pos_y"] += ball_value["to_y"]

    # 4. Dealing with collision 
    # update chracter's rect info   
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_index, ball_value in enumerate(balls) : 
        ball_pos_x = ball_value["pos_x"]
        ball_pos_y = ball_value["pos_y"]
        ball_img_index = ball_value["img_index"]

        # update ball's rect info
        ball_rect = ball_images[ball_img_index].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # collision between ball and character
        if character_rect.colliderect(ball_rect) :
            running = False
            break
        
        # collision between ball and weapon
        for weapon_index, weapon_value in enumerate(weapons) : 
            weapon_pos_x = weapon_value[0]
            weapon_pos_y = weapon_value[1]
            
            # update weapon's rect info 
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_x_pos
            weapon_rect.top = weapon_y_pos

            # check collision
            if weapon_rect.colliderect(ball_rect) :
                weapon_to_remove = weapon_index # to reamove the current weapon
                ball_to_remove = ball_index # to remove the current ball
                # break
    
    # remove the collided ball and weapon
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1

    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    # 5. Draw on the window
    screen.blit(background,(0,0))

    for weapon_x_pos, weapon_y_pos in weapons :
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    
    for index, value in enumerate(balls):
        ball_pos_x = value["pos_x"]
        ball_pos_y = value["pos_y"]
        ball_img_index = value["img_index"]
        screen.blit(ball_images[ball_img_index], (ball_pos_x, ball_pos_y))
    
    screen.blit(stage, (0,screen_height-stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    

    pygame.display.update() # redraw the background


# game finished
pygame.quit()
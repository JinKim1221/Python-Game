import pygame

pygame.init() # neccessary initialization

# screen setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# background setting
background = pygame.image.load("C:/Users/Jin/Desktop/Python_game/pygame_basic/background.png")

# set title
pygame.display.set_caption("Python Game")

# Event loop to prevent closing the window
running = True # game is running
while running:
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False

    # screen.fill((20, 210, 255)) 
    screen.blit(background, (0,0)) # draw the background
    pygame.display.update() # redraw the background

# game finished
pygame.quit()
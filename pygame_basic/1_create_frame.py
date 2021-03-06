import pygame

pygame.init() # neccessary initialization

# screen setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# set title
pygame.display.set_caption("Python Game")

# Event loop to prevent closing the window
running = True # game is running
while running:
    for event in pygame.event.get(): # what kind of event occured?
        if event.type == pygame.QUIT: # the event is that when closing the window
            running = False

# game finished
pygame.quit()
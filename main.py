# main file for Cellular Automata using Conways Game of life
import pygame
from com.mjp.cellular_automata.cell_grid import CellGrid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill("purple")
clock = pygame.time.Clock()
running = True
cellGrid = CellGrid(50, 50)
gridList = cellGrid.init_grid(screen)
pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("black")

    # flip() the display to put your work on screen
    # pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()
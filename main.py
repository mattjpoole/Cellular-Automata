# main file for Cellular Automata using Conways Game of life
import pygame
from com.mjp.cellular_automata.cell_grid import CellGrid

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill("purple")
clock = pygame.time.Clock()
running = True
cellGrid = CellGrid(70, 10)
gridList = cellGrid.init_grid(screen)
pygame.display.flip()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # run the gane rules or re-init per tick
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cellGrid.run_rules(gridList, screen)
        pygame.display.flip()
    if keys[pygame.K_i]:
        gridList = cellGrid.init_grid(screen)
        pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()
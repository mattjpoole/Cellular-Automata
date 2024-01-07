# main file for Cellular Automata using Conways Game of life
import pygame
from com.mjp.cellular_automata.cell_grid import CellGrid
from com.mjp.cellular_automata.grid_rect import GridRect

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill("purple")
clock = pygame.time.Clock()
running = True
width = 50
height = 50
cellGrid = CellGrid(width, height)
gridList = cellGrid.init_grid(screen)
# use full cell grid
#grid_rect = GridRect(0,0,width, height)
# use smaller grid
grid_rect = GridRect(20, 20, 30, 30)
cellGrid.set_random_pattern(gridList, screen, grid_rect)

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
        cellGrid.reset_grid(gridList, screen)
        cellGrid.set_random_pattern(gridList, screen, grid_rect)
        pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

pygame.quit()
# main file for Cellular Automata using Conways Game of life
import pygame
import pygame_gui
from com.mjp.cellular_automata.cell_grid import CellGrid
from com.mjp.cellular_automata.grid_rect import GridRect
from com.mjp.mvc.controller import Keyboard
from com.mjp.mvc.eventmanager import *
from com.mjp.mvc.model import GameEngine
from com.mjp.mvc.view import GraphicalView

# pygame setup

"""pygame.init()

screen = pygame.display.set_mode((1280, 720))
screen.fill("purple")
clock = pygame.time.Clock()
running = True


# gui set up
ui_manager = pygame_gui.UIManager((1280, 720))
reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 670), (100, 50)),
                                             text='RESET',
                                             manager=ui_manager)
run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 670), (100, 50)),
                                             text='RUN',
                                             manager=ui_manager)
pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 670), (100, 50)),
                                             text='PAUSE',
                                             manager=ui_manager)

# app set up
rules_running = False
width = 50
height = 50
cellGrid = CellGrid(width, height)
gridList = cellGrid.init_grid(screen)
# use full cell grid
# grid_rect = GridRect(0,0,width, height)
# use smaller grid
grid_rect = GridRect(20, 20, 30, 30)
cellGrid.set_random_pattern(gridList, screen, grid_rect)
"""

#example MVC set up
evManager = EventManager()
gamemodel = GameEngine(evManager)
keyboard = Keyboard(evManager, gamemodel)
graphics = GraphicalView(evManager, gamemodel)
gamemodel.run()

"""
pygame.display.flip()

while running:
    # limits FPS to 60
    time_delta = clock.tick(60)/1000.0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == reset_button:
                cellGrid.reset_grid(gridList, screen)
                cellGrid.set_random_pattern(gridList, screen, grid_rect)
            if event.ui_element == run_button:
                rules_running = True
            if event.ui_element == pause_button:
                rules_running = False
        ui_manager.process_events(event)

    # run the gane rules or re-init per tick
    if rules_running:
        cellGrid.run_rules(gridList, screen)

    ui_manager.update(time_delta)
    ui_manager.draw_ui(screen)
    pygame.display.flip()
    

pygame.quit()"""
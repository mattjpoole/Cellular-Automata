import pygame
from com.mjp.mvc.model import GameEngine
from com.mjp.mvc.eventmanager import *
from com.mjp.cellular_automata.cell_grid import CellGrid
from com.mjp.cellular_automata.grid_rect import GridRect

class GraphicalView(object):
    """
    Draws the model state onto the screen.
    """

    def __init__(self, evManager, model, screen):
        """
        evManager (EventManager): Allows posting messages to the event queue.
        model (GameEngine): a strong reference to the game Model.
                
        Attributes:
        isinitialized (bool): pygame is ready to draw.
        screen (pygame.Surface): the screen surface.
        clock (pygame.time.Clock): keeps the fps constant.
        """
        
        self.evManager:EventManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.isinitialized = False
        self.screen = screen
        self.clock = None
        self.width = None
        self.height = None
        self.gridList = []
        self.cellGrid:CellGrid = None
        self.grid_rect:GridRect = None
    
    def notify(self, event):
        """
        Receive events posted to the message queue. 
        """
        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, QuitEvent):
            # shut down the pygame graphics
            self.isinitialized = False
            pygame.quit()
        elif isinstance(event, TickEvent):
            self.renderall()
            # limit the redraw speed to 30 frames per second
            self.clock.tick(30)
    
    def renderall(self):
        """
        Draw the current game state on screen.
        Does nothing if isinitialized == False (pygame.init failed)
        """

        if not self.isinitialized:
            return

        # run the rules
        self.cellGrid.run_rules(self.gridList, self.screen)

        # flip the display to show whatever we drew
        pygame.display.flip()
        
    def initialize(self):
        """
        Set up the pygame graphical display and loads graphical resources.
        """

        pygame.display.set_caption('Game of Life')
        self.clock = pygame.time.Clock()
        self.isinitialized = True

        self.width = 50
        self.height = 50
        self.cellGrid = CellGrid(self.width, self.height)
        self.gridList = self.cellGrid.init_grid(self.screen)
        # use full cell grid
        # self.grid_rect = GridRect(0,0,width, height)
        # use smaller grid
        self.grid_rect = GridRect(20, 20, 30, 30)
        self.cellGrid.set_random_pattern(self.gridList, self.screen, self.grid_rect)
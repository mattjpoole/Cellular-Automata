import pygame
import pygame_gui
from com.mjp.mvc.model import GameEngine
from com.mjp.mvc.eventmanager import *

class UIControls():
    
    def __init__(self, evManager, model, screen) -> None:
        """initialise the class object"""
        self.evManager:EventManager = evManager
        evManager.RegisterListener(self)
        self.model = model
        self.clock = None
        self.isinitialized = False
        self.screen = screen
        self.ui_manager:pygame_gui.UIManager = None
        self.reset_button = None
        self.run_button = None
        self.pause_button = None

    def notify(self, event):
        """
        Receive events posted to the message queue. 
        """
        if isinstance(event, InitializeEvent):
            self.initialize()
        elif isinstance(event, TickEvent):
            self.renderall()

    def initialize(self):
        """
        Set up the ui controls display
        """
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.get_surface()

        self.ui_manager = pygame_gui.UIManager((1280, 720))
        self.reset_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((0, 670), (100, 50)),
                                                    text='RESET',
                                                    manager=self.ui_manager)
        self.run_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((100, 670), (100, 50)),
                                                    text='RUN',
                                                    manager=self.ui_manager)
        self.pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((200, 670), (100, 50)),
                                                    text='PAUSE',
                                                    manager=self.ui_manager)
    
    def renderall(self):
        """render the buttons on TickEvent"""
        time_delta = self.clock.tick(60)/1000.0

        self.ui_manager.update(time_delta)
        self.ui_manager.draw_ui(self.screen)
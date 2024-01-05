import pygame

class Cell:

    def __init__(self, alive, rect, out_of_bounds=False):
        self.alive = alive
        self.rect = rect
        self.out_of_bounds = out_of_bounds

    def is_alive(self) -> bool:
        return self.alive
    
    def set_alive(self, alive):
        self.alive = alive
    
    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def is_out_of_bounds(self) -> bool:
        return self.out_of_bounds
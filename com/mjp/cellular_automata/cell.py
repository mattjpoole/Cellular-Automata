import pygame

class Cell:

    SIZE = 8
    COLOUR_ALIVE = [0, 0, 0, 255]
    COLOUR_DEAD = [255, 255, 255, 255]


    def __init__(self, alive, rect, out_of_bounds=False):
        self.alive = alive
        self.rect = rect
        self.out_of_bounds = out_of_bounds
        self.column = 0
        self.row = 0

    def is_alive(self) -> bool:
        return self.alive
    
    def set_alive(self, alive):
        self.alive = alive
    
    def get_rect(self) -> pygame.Rect:
        return self.rect
    
    def is_out_of_bounds(self) -> bool:
        return self.out_of_bounds
    
    def set_coords(self, column, row):
        self.column = column
        self.row = row
   
    def get_column(self)->int:
        return self.column
    
    def get_row(self)->int:
        return self.row
    
import random
import pygame

class CellGrid:
    """A utility class for updating the grid of cells according to Conways Game of Life rules"""

    def __init__(self, width, height) -> None:
        """Initialise the class and screen object"""
        self.width = width
        self.height = height

    def init_grid(self, screen) -> list:
        """Create a random staring pattern of cells"""
        total = self.width * self.height
        rect_width_height = 10
        grid_list = []
        i = 0
        j = 0
        top = left = i
        while i<total:
            if random.randint(0, 1) == 1:
                colour = [255, 255, 255, 255]
            else:
                colour = [0, 0, 0, 255]
            cell = pygame.draw.rect(screen, colour, [left, top, rect_width_height, rect_width_height])
            grid_list.append(cell)
            i += 1
            if i % self.width == 0:
                j += 1
            left = (i % self.width) * rect_width_height
            top = j * rect_width_height
            print()

        return grid_list
 
    def apply_rules(self) -> None:
        """Method to apply Conways Game of life rules each tick"""
        #Any live cell with fewer than two live neighbours dies, as if by underpopulation
        #Any live cell with two or three live neighbours lives on to the next generation
        #Any live cell with more than three live neighbours dies, as if by overpopulation
        #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

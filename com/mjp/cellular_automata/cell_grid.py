import pygame

class CellGrid:
    """A utility class for updating the grid of cells according to Conways Game of Life rules"""

    def __init__(self, width, height) -> None:
        """Initialise the class and screen object"""
        self.width = width
        self.height = height

    def initGrid(self, screen) -> list:
        total = self.width * self.height
        rectWidthHeight = 10
        gridList = []
        i = 0
        top = left = i
        while i<total:
            cell = pygame.draw.rect(screen, [255, 255, 255, 255], [top, left, rectWidthHeight, rectWidthHeight])
            gridList.append(cell)
            i += 1
            top = i * rectWidthHeight
            left = i * rectWidthHeight

        return gridList

    
    def applyRules() -> None:
        """Method to apply Conways Game of life rules each tick"""
        #Any live cell with fewer than two live neighbours dies, as if by underpopulation
        #Any live cell with two or three live neighbours lives on to the next generation
        #Any live cell with more than three live neighbours dies, as if by overpopulation
        #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction

import random
import pygame
from com.mjp.cellular_automata.cell import Cell

class CellGrid:
    """A utility class for updating the grid of cells according to Conways Game of Life rules"""

    def __init__(self, width, height) -> None:
        """Initialise the class and screen object"""
        self.width = width
        self.height = height
    
    def init_grid(self, screen) -> list:
        """Create a feild of dead cells ready to recoeve a pattern"""
        total = self.width * self.height
        grid_list = []
        column = top = left = cell_num = row = 0
        while cell_num<total:
            rect = pygame.draw.rect(screen, Cell.COLOUR_DEAD, [left, top, Cell.SIZE, Cell.SIZE])
            cell = Cell(False, rect)
            cell.set_coords(column, row)
            grid_list.append(cell)
            # prepare for next loop
            cell_num += 1
            column = cell_num % self.width
            if column == 0:
                row += 1
            left = column * Cell.SIZE
            top = row * Cell.SIZE
        return grid_list
    
    def set_random_pattern(self, grid_list, screen) -> None:
        """set a random pattern on the grid""" 
        i = 0
        while i < len(grid_list):
            kernel : Cell = grid_list[i]
            if random.randint(0, 1) == 0:
                kernel.set_alive(True)
                screen.fill("black", kernel.get_rect())
            i += 1

    def run_rules(self, grid_list, screen) -> None:
        """Method to apply Conways Game of life rules each tick"""
        i = 0
        while i < len(grid_list):
            kernel : Cell = grid_list[i]
            neighbours = self.get_neighbours(grid_list, i)
            alive_neighbours = 0
            cell : Cell
            for cell in neighbours:
                if cell.is_out_of_bounds() is False:
                    if cell.is_alive():
                        alive_neighbours += 1
        
            if kernel.is_alive():
                #check alive neighbours
                if alive_neighbours < 2 or alive_neighbours >3:
                    #Any live cell with fewer than two live neighbours dies, as if by underpopulation
                    #Any live cell with greter than three live neighbours dies, as if by overpopulation
                    print ("kernel: "+str(i)+" dies")
                    kernel.set_alive(False)
                    screen.fill("white", kernel.get_rect())
                else:
                    #Any live cell with two or three live neighbours lives on to the next generation
                    print ("kernel: "+str(i)+" lives on")
            else:
                if alive_neighbours == 3:    
                    #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
                    print ("kernel: "+str(i)+" comes alive")
                    kernel.set_alive(True)
                    screen.fill("black", kernel.get_rect())
            alive_neighbours = 0
            i += 1

                
    def get_neighbours(self, grid_list, cell_index) -> list:
        """Method to select neighbouring cells for give cell"""
        out_of_bounds_rect = pygame.Rect(0,0,0,0)
        top_left = top_middle = top_right = middle_left = middle_right = bottom_left = bottom_middle = bottom_right = Cell(False, out_of_bounds_rect, True)
        kernel = grid_list[cell_index]
        try:
            # if we are not at the top edge
            if kernel.get_row()>0:
                top_middle = grid_list[cell_index-self.width]
                # and we are not at the left edge
                if kernel.get_column()>0:
                    top_left = grid_list[cell_index-self.width+1]
                # and we are not at the right edge
                if kernel.get_column()<self.width-1:
                    top_right = grid_list[cell_index-self.width-1]
            
            # if we are not on the left edge
            if kernel.get_column()>0:
                middle_left = grid_list[cell_index-1]
             
            # if we are not on the right edge
            if kernel.get_column()<self.width-1:
                middle_right = grid_list[cell_index+1]
            
            # if we are not the bottom edge
            if kernel.get_row() < self.height-1:
                bottom_middle = grid_list[cell_index+self.width]
                # and we are not on the left edge
                if kernel.get_column()>0:
                    bottom_left = grid_list[cell_index+self.width-1]
                # and we are not at the right edge
                if (kernel.get_column()<self.width-1):
                    bottom_right = grid_list[cell_index+self.width+1]

        except IndexError:
            print("cell index out of bounds ====")
            print("kernel.get_column()"+str(kernel.get_column()))
            print("kernel.get_row()"+str(kernel.get_row()))
        neighbours = [top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]
        return neighbours

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
        """Create a random staring pattern of cells"""
        total = self.width * self.height
        grid_list = []
        i = 0
        j = 0
        top = left = i
        alive = True
        while i<total:
            if random.randint(0, 1) == 0:#1:
                colour = [255, 255, 255, 255]
                alive = True
            else:
                colour = [0, 0, 0, 255]
                alive = False
            rect = pygame.draw.rect(screen, colour, [left, top, Cell.SIZE, Cell.SIZE])
            grid_list.append(Cell(alive, rect))
            i += 1
            if i % self.width == 0:
                j += 1
            left = (i % self.width) * Cell.SIZE
            top = j * Cell.SIZE

        return grid_list
 
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
                    #screen.fill("black", kernel)
                    screen.fill("white", kernel)
                else:
                    #Any live cell with two or three live neighbours lives on to the next generation
                    print ("kernel: "+str(i)+" lives on")
            else:
                if alive_neighbours == 3:    
                    #Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
                    print ("kernel: "+str(i)+" comes alive")
                    kernel.set_alive(True)
                    #screen.fill("white", kernel)
                    screen.fill("black", kernel)
            alive_neighbours = 0
            i += 1

                
    def get_neighbours(self, grid_list, cell_index) -> list:
        """Method to select neighbouring cells for give cell"""
        out_of_bounds_rect = pygame.Rect(0,0,0,0)
        top_left = top_middle = top_right = middle_left = middle_right = bottom_left = bottom_middle = bottom_right = Cell(False, out_of_bounds_rect, True)
        try:
            if cell_index-self.width>0:
                print("cell_index: "+str(cell_index)+" "+str(cell_index%self.width))
                if (cell_index%self.width>0):
                    top_left = grid_list[cell_index-self.width-1]
                top_middle = grid_list[cell_index-self.width]
                if (cell_index%self.width<self.width):
                    top_right = grid_list[cell_index-self.width+1]
            if cell_index-1 >= 0:
                if (cell_index%self.width>0):
                    middle_left = grid_list[cell_index-1]
            if cell_index+1 < self.width*self.height:
                if (cell_index%self.width<self.width):
                    middle_right = grid_list[cell_index+1]
            if cell_index+self.width<self.width*self.height+1:
                if (cell_index%self.width>0):
                    bottom_left = grid_list[cell_index+self.width-1]
                bottom_middle = grid_list[cell_index+self.width]
                if (cell_index%self.width<self.width):
                    bottom_right = grid_list[cell_index+self.width+1]
        except IndexError:
            print("cell index out of bounds")
        neighbours = [top_left, top_middle, top_right, middle_left, middle_right, bottom_left, bottom_middle, bottom_right]
        return neighbours   

from com.mjp.cellular_automata.cell import Cell

class GridRect:
    """a class to represent a rectangle of coordinates on the CellGrid""" 

    def __init__(self, top, left, bottom, right) -> None:
        """Initialise the class object"""
        self.top = top
        self.left = left
        self.bottom = bottom
        self.right = right
    
    def get_top(self) -> int:
        return self.top
    
    def get_left(self) -> int:
        return self.left
    
    def get_bottom(self) -> int:
        return self.bottom
    
    def get_right(self) -> int:
        return self.right

    def contains_cell(self, cell:Cell) -> bool:
        """check to see whether the passed cell is within this GridRect"""
        col_intersects = cell.get_column()>= self.left and cell.get_column()<self.right
        row_intersects = cell.get_row()>=self.top and cell.get_row()<self.bottom
        return col_intersects and row_intersects


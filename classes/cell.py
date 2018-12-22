#! /usr/bin/env python3
# coding: utf-8

class Cell:
    """Represents a cell that contain an element of the game (or not)
    
    Attributes:
    :pos_x: x position of the cell on the grid of the level
    :pos_y: y position of the cell on the grid of the level
    :element: element that the cell contains (wall, needle... etc)"""

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.element = None


# ----------------------------------------------------------------
#                            METHODS
# ----------------------------------------------------------------


    def getCellInformation(self):
        """Display information about the cell in the terminal"""
        print("Cell ["+str(self.pos_x)+","+str(self.pos_y)+"] : "+self.element.name)

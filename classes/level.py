#! /usr/bin/env python3
# coding: utf-8
import os
import path

class Level:
    """Represents the levels of the game
    
    Attributes:
    :numLevel: Number of the level. (int)
    :csvPath: Path to find the csv where the level is contained. (string)
    :csvGrid: Grid that contains all the symbols loaded from the csv. (list of lists)"""

    def __init__(self, numLevel):
        self.numLevel = numLevel

        self._csvPath = str()
        self._set_CSV_Path()

        self._csvGrid = list()
        self._set_CSV_Grid()

# ----------------------------------------------------------------
#                            SETTERS/GETTERS
# ----------------------------------------------------------------



    def _get_CSV_Path(self):
        """Get the csv path"""
        return self._csvPath



    def _set_CSV_Path(self):
        """Set the csv path """

        fileName = "level"+str(self.numLevel)+".csv"
        self._csvPath = path.setPath("resources/levels",fileName)



    def _get_CSV_Grid(self):
        """Getters for the csv grid"""
        return self._csvGrid



    def _set_CSV_Grid(self):
        """Setters for the csv grid"""

        with open(self._get_CSV_Path(), "r") as csvFile:
            for line in csvFile:
                self._csvGrid.append(line)



    csvPath = property(_get_CSV_Path, _set_CSV_Path)
    csvGrid = property(_get_CSV_Grid, _set_CSV_Grid)


# ----------------------------------------------------------------
#                            METHODS
# ----------------------------------------------------------------
    
    def printCSVGrid(self):
        """Print the csv grid on the terminal"""

        try:
            for line in self._csvGrid:
                print(line)

        except:
            print("The Grid couldn't be printed on terminal")

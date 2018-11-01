#! /usr/bin/env python3
# coding: utf-8


# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------


#Python library
import os
import pygame
from pygame.locals import *
import random


#My own library
from classes.cell import Cell
from classes.element import Element
import path

class Level:
    """Represents the levels of the game
    
    Attributes:
    :numLevel: Number of the level. (int)
    :csvPath: Path to find the csv where the level is contained. (string)
    :csvGrid: Grid that contains all the symbols loaded from the csv. (list of lists)
    :tilesPath: Path to the png file of the tiles (string)
    :element: list of the elements in the level"""

    def __init__(self, numLevel):
        self.numLevel = numLevel

        self._csvPath = str()
        self._set_CSV_Path()

        self._csvGrid = list()
        self._set_CSV_Grid()

        self._tilesPath = None
        self._set_tiles_path()

        self._elements = list()
        self._set_elements()

        self._cells = list()
        self._set_cells(15, 15)

        self.randElementInCells()


# ----------------------------------------------------------------
#                            SETTERS/GETTERS
# ----------------------------------------------------------------



    def _get_cells(self):
        """Return the list of the cells of the level"""
        return self._cells



    def _set_cells(self, size_width, size_height):
        """Set the list of the cells of the level"""

        i = 0
    
        while i < size_height:
            rowCells = list()
            j = 0

            while j < size_width:
                rowCells.append(Cell(j,i))
                j = j + 1

            i = i + 1
            self._cells.append(rowCells)


    def _get_CSV_Path(self):
        """Get the csv path"""
        return self._csvPath



    def _set_CSV_Path(self):
        """Set the csv path depending on the number of the level"""

        fileName = "level"+str(self.numLevel)+".csv"
        self._csvPath = path.setPath("resources/levels",fileName)



    def _get_CSV_Grid(self):
        """Getters for the csv grid"""
        return self._csvGrid



    def _set_CSV_Grid(self):
        """Setters for the csv grid"""

        with open(self._get_CSV_Path(), "r") as csvFile:
            for line in csvFile:
                lineList = line.split(",")
                lineList[len(lineList)-1] = lineList[len(lineList)-1].replace("\n", "")
                
                self._csvGrid.append(lineList)



    def _get_elements(self):
        """Get the list of elements of the level"""
        return self._elements



    def _set_elements(self):
        """Set the list of elements that are contained in the level"""

        self._elements.append(Element("Needle", False))
        self._elements.append(Element("Tube", False))
        self._elements.append(Element("Ether", False))



    def _get_tiles_path(self):
        """Get the tiles"""
        return self._tilesPath



    def _set_tiles_path(self):
        """Set the tiles"""

        #Loading the image for the tiles
        self._tilesPath = path.setPath("resources/img","floor-tiles-20x20.png")




    csvPath = property(_get_CSV_Path, _set_CSV_Path)
    csvGrid = property(_get_CSV_Grid, _set_CSV_Grid)
    cells = property(_get_cells, _set_cells)
    elements = property(_get_elements, _set_elements)
    tiles = property(_get_tiles_path, _set_tiles_path)


# ----------------------------------------------------------------
#                            METHODS
# ----------------------------------------------------------------

    def setCSVCell(self, x, y, symbol):
        """Set an element symbol in the csv grid"""
        self._csvGrid[y][x] = symbol

    def setTilesOnScreen(self, window):
        """Display the tiles of the level on the window of the game"""
        i = 0

        #We load the image where the tiles are
        tileImage = pygame.image.load(self._get_tiles_path()).convert_alpha()

        #In the image, there are a lot of tiles. We will create a surface to crop just one tile.
        surface = pygame.Surface((20,20))

        #We place the image on the surface and crop it
        surface.blit(tileImage, (0,0), (0,0,20,20))

        while i < 15:

            j = 0
            while j < 15:

                #Load only part of an image
                #https://stackoverflow.com/questions/38535330/load-only-part-of-an-image-in-pygame
                window.blit(tileImage, (i*20,j*20), (0,0,20,20))

                j = j + 1
            i = i + 1
        
        pygame.display.flip()



    def printCSVGrid(self):
        """Print the csv grid on the terminal"""

        try:
            for line in self._csvGrid:
                print(line)

        except:
            print("The Grid couldn't be printed on terminal")



    def randElementInCells(self):
        """Insert elements of the level in random cells"""


        #We are going to place each element in a cell
        for element in self._get_elements():
            randAgain = True

            #We generate a random position. If the cell is already taken, we generate another one
            while randAgain == True:
                x = random.randint(0, 14)
                y = random.randint(0, 14)
                #print("x : "+str(x))
                #print("y : "+str(y))
                #print("cell : "+self._get_CSV_Grid()[y][x])

                if self._get_CSV_Grid()[y][x] == "":
                    self._cells[y][x].element = element
                    self.setCSVCell(x, y, element._get_CSV_symbol())
                    print(element.name+" is on cell : ["+str(x)+","+str(y)+"]")
                    randAgain = False

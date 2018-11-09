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
import readJSON

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
        self.guardianCoordinates = tuple()
        self._set_cells(15, 15)

        self.playerCoordinates = tuple()

        self.randElementInCells()
        self.setCellsFromCSV()


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

        self._elements.append(Element("Needle"))
        self._elements.append(Element("Tube"))
        self._elements.append(Element("Ether"))



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



    def checkIfPlayerIsOutOfGrid(self, nextPlayerPosition):
        """We check if the player is out of the grid of the level"""

        playerOutOfGrid = bool()

        if pos_x < 0 or pos_x >= len(self._get_cells()[0]) or pos_y < 0 or pos_y >= len(self._get_cells()):
            playerOutOfGrid = True

        else:
            playerOutOfGrid = False

        return playerOutOfGrid



    def checkIfMovementIsValid(self, nextPlayerPosition):
        """We check if the player can move according to the key he has pressed."""

        pos_x = nextPlayerPosition[0]
        pos_y = nextPlayerPosition[1]
        movementIsValid = bool()


        if self.checkIfPlayerIsOutOfGrid == True:
            print("Player is out of the grid")
            movementIsValid = False


        #If the player is not out of the grid
        else:
            print("Player is in the grid")
            cell = self._get_cells()[pos_y][pos_x]
            if cell.element is not None:
                if cell.element.blockThePlayer == True:
                    movementIsValid = False
                
                else:
                    movementIsValid = True

            else:
                movementIsValid = True
        
        print("Movement is valid : "+str(movementIsValid))
        return movementIsValid



    def checkIfPlayerIsOnElement(self, nextPlayerPosition):
        """Check if the player will be on an element that will help him to end the level"""

        pos_x = nextPlayerPosition[0]
        pos_y = nextPlayerPosition[1]

        elementToCheck = self._get_cells()[pos_y][pos_x].element

        if elementToCheck is not None:
            print("Element to check : "+elementToCheck.name)

        for element in self._get_elements():
            if elementToCheck is not None and elementToCheck.name == element.name:
                print("Player got the "+element.name)
                self._get_elements().remove(element)



    def checkIfPlayerIsOnGuardian(self, nextPlayerPosition):
        """We check if the player has reached the guardian (end of the level).
        If he reaches him and has all the element (len(self._getelements()) == 0, then he has won"""

        playerWin = bool()

        print("Guardian coordinates")
        print(self.guardianCoordinates)

        #If the player will reach the guardian
        if nextPlayerPosition == self.guardianCoordinates:
            print("Next player position equals guardian position")

            #If he has all the elements (needle, tube and ether), he wins
            if len(self._get_elements()) == 0:
                print("Playerwin = true : method")
                playerWin = True

            #If he doesn't have all the elements, he loses
            else:
                playerWin = False

        #If he will not reach the guardian at the next move
        else:
            playerWin = None

        return playerWin
        



    def editCellAndGrid(self, element, oldPosition, newPosition):
        """Edit the csvGrid and the cells with the new coordinates of an element"""

        old_x = oldPosition[0]
        old_y = oldPosition[1]
        new_x = newPosition[0]
        new_y = newPosition[1]

        #We empty the previous cell
        self._get_CSV_Grid()[old_y][old_x] = ""
        self._get_cells()[old_y][old_x].element = None

        #We fill the new cell
        self._get_CSV_Grid()[new_y][new_x] = element._get_CSV_symbol()
        self._get_cells()[new_y][new_x].element = element


    
    def movePlayer(self, nextPlayerPosition):
        """Move the player on the coordinates nextPlayerPosition"""

        old_x = self.playerCoordinates[0]
        old_y = self.playerCoordinates[1]

        self.editCellAndGrid(self._get_cells()[old_y][old_x].element, self.playerCoordinates, nextPlayerPosition)

        self.playerCoordinates = nextPlayerPosition



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



    def setCellsFromCSV(self):
        """Set the elements of the csv list into the cell list"""
        i = 0
        for line in self._get_CSV_Grid():
            j = 0

            for cellcsv in line:
                #If the cell in the csv is not empty
                if cellcsv == "":
                    pass

                elif cellcsv == "P":
                    self._cells[i][j] = Cell(j, i)
                    self._cells[i][j].element = Element("MacGyver")
                    self.playerCoordinates = (j, i)

                elif cellcsv == "G":
                    self._cells[i][j] = Cell(j, i)
                    self._cells[i][j].element = Element("Guardian")
                    self.guardianCoordinates = (j, i)                  

                else:
                    symbolDict = readJSON.jsonToDictionary("resources", "element.json")
                    elementName = Element.getNameFromSymbolInDict(symbolDict, cellcsv)
                    self._cells[i][j] = Cell(j, i)
                    self._cells[i][j].element = Element(elementName)
                j = j + 1
            
            i = i + 1
                    
        



    def setCSVCell(self, x, y, symbol):
        """Set an element symbol in the csv grid"""
        self._csvGrid[y][x] = symbol



    def setElementsOnScreen(self, window):
        """Set elements of the level on the window screen"""
        i = 0
        #We go through the csv grid
        for line in self._get_cells():
            j = 0

            for cell in line:
                if cell.element is not None:
                    elementImage = pygame.image.load(cell.element._get_skin())
                    window.blit(elementImage, (j*40, i*40))
                
                j = j + 1
            
            i = i + 1
        pygame.display.flip()
        



    def setTilesOnScreen(self, window, heightGrid, widthGrid):
        """Display the tiles of the level on the window of the game"""
        i = 0

        #We load the image where the tiles are
        tileImage = pygame.image.load(self._get_tiles_path()).convert_alpha()

        #In the image, there are a lot of tiles. We will create a surface to crop just one tile.
        surface = pygame.Surface((20,20))

        #We place the image on the surface and crop it
        surface.blit(tileImage, (0,0), (0,0,20,20))

        while i < heightGrid * 2:

            j = 0
            while j < widthGrid * 2:

                #Load only part of an image
                #https://stackoverflow.com/questions/38535330/load-only-part-of-an-image-in-pygame
                window.blit(tileImage, (i*20,j*20), (0,0,20,20))

                j = j + 1
            i = i + 1
        
        pygame.display.flip()

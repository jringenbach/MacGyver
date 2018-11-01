#! /usr/bin/env python3
# coding: utf-8


# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------


#Python library
import pygame
from pygame.locals import *
import os

#My own library
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

        self._tilesPath = None
        self._set_tiles_path()

# ----------------------------------------------------------------
#                            SETTERS/GETTERS
# ----------------------------------------------------------------



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
                self._csvGrid.append(line)



    def _get_tiles_path(self):
        """Get the tiles"""
        return self._tilesPath



    def _set_tiles_path(self):
        """Set the tiles"""

        #Loading the image for the tiles
        self._tilesPath = path.setPath("resources/img","floor-tiles-20x20.png")
        print(self._tilesPath)




    csvPath = property(_get_CSV_Path, _set_CSV_Path)
    csvGrid = property(_get_CSV_Grid, _set_CSV_Grid)
    tiles = property(_get_tiles_path, _set_tiles_path)


# ----------------------------------------------------------------
#                            METHODS
# ----------------------------------------------------------------
    def setTilesOnScreen(self, window):
        """Display the tiles of the level on the window of the game"""
        i = 0

        #We load the image where the tiles are
        tileImage = pygame.image.load(self._get_tiles_path()).convert_alpha()

        #In the image, there are a lot of tiles. We will create a surface to crop just one tile.
        surface = pygame.Surface((20,20))

        #We place the image on the surface and crop it
        self._tiles = surface.blit(tileImage, (0,0), (0,0,20,20))

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

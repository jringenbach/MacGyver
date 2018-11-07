#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

#python modules
import pygame
from pygame.locals import *

def playerMovement(event, level):
    """Treats the movement of the player"""

    nextPlayerPosition = tuple()

    if event.key == K_LEFT:
        print("Player goes left.")
        nextPlayerPosition = (level.playerCoordinates[0] - 1, level.playerCoordinates[1])

    elif event.key == K_RIGHT:
        print("Player goes right.")
        nextPlayerPosition = (level.playerCoordinates[0] + 1, level.playerCoordinates[1])

    elif event.key == K_UP:
        print("Player goes up.")
        nextPlayerPosition = (level.playerCoordinates[0], level.playerCoordinates[1] - 1)

    elif event.key == K_DOWN:
        print("Player goes down.")
        nextPlayerPosition = (level.playerCoordinates[0], level.playerCoordinates[1] + 1)

    else:
        print("The player pressed a key.")


    print(nextPlayerPosition)
    return nextPlayerPosition



def titleScreenKeydown(event):
    """Handle the keydown event during the title screen"""
    
    continuer = True

    #The player choses to play a new game
    if event.key == K_KP1:
        continuer = False

    return continuer
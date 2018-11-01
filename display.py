#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

#Python modules
import pygame
from pygame.locals import *

#My own modules
from classes.level import Level
import eventHandler

# ----------------------------------------------------------------
#                           METHODS
# ----------------------------------------------------------------

def displayTitleScreen(conf, window):
    """Display the title screen in the window"""

    continuer = True
    playerChoice = None

    #Methods to display the title screen in the window
    titleScreen = pygame.image.load(conf["title_screen_path"]).convert()
    window.blit(titleScreen, (0,0))
    pygame.display.flip()

    #Actions to do when an event is fired
    while continuer:
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                print("A key has been pressed : "+str(event.key))
                continuer = eventHandler.titleScreenKeydown(event)
                playerChoice = "1"

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                continuer = False
                playerChoice = "1"

            elif event.type == QUIT:
                print("Goodbye!")
                continuer = False

    print(playerChoice)
    return playerChoice



def displayLevel(numLevel):
    """Display the level of the game"""

    quit_game = False
    keep_playing = True
    level = Level(numLevel)
    level.printCSVGrid()
    print("display level : level "+str(level.numLevel))

    #While the level is not over
    while keep_playing:
        
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                pass
            
            elif event.type == QUIT:
                print("Goodbye")
                keep_playing = False #We exit the cycle where we listen for events
                quit_game = True #We exit the cycle of the game
    
    return quit_game
    
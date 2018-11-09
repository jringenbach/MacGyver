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



def displayLevel(numLevel, window):
    """Display the level of the game"""

    #Method variables
    quit_game = False
    keep_playing = True
    levelRestart = True
    playerWin = bool()





    #background = pygame.image.load("resources/img/fond.jpg").convert()
    #window.blit(background, (0,0))
    #pygame.display.flip()

    while levelRestart:
    #While the level is not over
        #Displaying the level
        level = Level(numLevel)
        print("Loading level : "+str(level.numLevel))
        keep_playing = True
        level.setTilesOnScreen(window, len(level._get_CSV_Grid()), len(level._get_CSV_Grid()[0]))
        level.setElementsOnScreen(window)

        while keep_playing:
            
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    nextPlayerPosition = eventHandler.playerMovement(event, level)

                    if nextPlayerPosition is not None:
                        movementIsValid = level.checkIfMovementIsValid(nextPlayerPosition)

                        if movementIsValid:
                            level.checkIfPlayerIsOnElement(nextPlayerPosition)
                            playerWin = level.checkIfPlayerIsOnGuardian(nextPlayerPosition)

                            if playerWin is None:
                                level.movePlayer(nextPlayerPosition)

                            elif playerWin == True:
                                print("Player wins.")
                                keep_playing = False
                                levelRestart = False

                            else:
                                keep_playing = False
                                levelRestart = True
                            

                            #Displaying the level
                            level.setTilesOnScreen(window, len(level._get_CSV_Grid()), len(level._get_CSV_Grid()[0]))
                            level.setElementsOnScreen(window)
                        print("--------- End of turn ---------")

                
                elif event.type == QUIT:
                    print("Goodbye")
                    keep_playing = False #We exit the cycle where we listen for events
                    quit_game = True #We exit the cycle of the game
                    levelRestart = False

    return quit_game
    
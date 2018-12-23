#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------#


#Python modules
import pygame
from pygame.locals import *

#My own modules
from classes.level import Level
import eventHandler

# ----------------------------------------------------------------
#                           METHODS
# ----------------------------------------------------------------

def display_image(imgPath, window):
    """Display the title screen in the window"""

    continuer = True
    playerChoice = None

    #Methods to display the title screen in the window
    titleScreen = pygame.image.load(imgPath).convert()
    window.blit(titleScreen, (0,0))
    pygame.display.flip()

    #Actions to do when an event is fired
    while continuer:
        for event in pygame.event.get():

            if event.type == KEYDOWN:
                print("A key has been pressed : "+str(event.key))
                continuer = eventHandler.title_screen_keydown(event)
                playerChoice = "1"

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                continuer = False
                playerChoice = "1"

            elif event.type == QUIT:
                print("Goodbye!")
                continuer = False

    print(playerChoice)
    return playerChoice


def display_level(numLevel, window):
    """Display the level of the game"""

    #Method variables
    quit_game = False
    keep_playing = True
    levelRestart = True
    playerWin = bool()
    gameStatus = dict()

    while levelRestart:
    #While the level is not over
        #Displaying the level
        level = Level(numLevel)
        print("Loading level : "+str(level.numLevel))
        keep_playing = True
        level.set_tiles_on_screen(window, len(level._get_CSV_Grid()), len(level._get_CSV_Grid()[0]))
        level.set_elements_on_screen(window)
        pygame.display.flip()


        while keep_playing:

            for event in pygame.event.get():
                if event.type == KEYDOWN and (event.key == K_LEFT or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_UP):
                    nextPlayerPosition = eventHandler.player_movement(event, level)

                    if nextPlayerPosition is not None:
                        movementIsValid = level.check_if_movement_is_valid(nextPlayerPosition)

                        if movementIsValid:
                            level.check_if_player_is_on_element(nextPlayerPosition)
                            playerWin = level.check_if_player_is_on_guardian(nextPlayerPosition)

                            if playerWin is None:
                                level.move_player(nextPlayerPosition)

                            elif playerWin == True:
                                print("Player wins.")
                                keep_playing = False
                                levelRestart = False

                            else:
                                print("Player loses")
                                keep_playing = False
                                levelRestart = False

                            level.set_tiles_on_screen(window, len(level._get_CSV_Grid()), len(level._get_CSV_Grid()[0]))
                            level.set_elements_on_screen(window)
                            pygame.display.flip()

                            
                        print("--------- End of turn ---------")

                
                elif event.type == QUIT:
                    print("Goodbye")
                    keep_playing = False #We exit the cycle where we listen for events
                    quit_game = True #We exit the cycle of the game
                    levelRestart = False

    gameStatus = { "quit_game" : quit_game,
    "playerWin" : playerWin
    }

    return gameStatus
    
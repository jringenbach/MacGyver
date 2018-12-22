#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

#python library
import os
import pygame
from pygame.locals import *

#My own methods
import display
import readJSON

# ----------------------------------------------------------------
#                      VARIABLE INITIALIZATION
# ----------------------------------------------------------------

conf = None
keep_playing = True
player_choice = None
gameStatus = dict()
gameStatus["quit_game"] = False
window = None

# ----------------------------------------------------------------
#                      CORE OF THE GAME
# ----------------------------------------------------------------

#Initialization of pygame
pygame.init()

#Center the window of the game at the center of the computer screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

#We get the configuration of the game and we set some properties
conf = readJSON.json_to_dictionary("", "conf.json")

#We set the window configuration
window = pygame.display.set_mode((conf["window_width"], conf["window_height"]))

#We display the title screen
player_choice = display.display_image(conf["title_screen_path"], window)

#Game cycle
while gameStatus["quit_game"] == False:
    print("boucle de jeu")

    #We launch the game
    if player_choice == "1":
        player_choice = None

        #At launch, we display the first level
        gameStatus = display.display_level(1, window)
        if gameStatus["quit_game"] != True:
            if gameStatus["playerWin"] == True:
                player_choice = display.display_image(conf["victory_path"], window)

            elif gameStatus["playerWin"] == False:
                player_choice = display.display_image(conf["defeat_path"], window)

            if player_choice is None:
                gameStatus["quit_game"] = True

    else:
        gameStatus["quit_game"] = True

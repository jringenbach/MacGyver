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
import configGame
import display
import readJSON

# ----------------------------------------------------------------
#                      VARIABLE INITIALIZATION
# ----------------------------------------------------------------

conf = None
keep_playing = True
player_choice = None
quit_game = False
window = None

# ----------------------------------------------------------------
#                      CORE OF THE GAME
# ----------------------------------------------------------------

#Initialization of pygame
pygame.init()

#Center the window of the game at the center of the computer screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

#We get the configuration of the game and we set some properties
conf = readJSON.jsonToDictionary()
conf = configGame.setConfiguration(conf)

#We set the window configuration
window = pygame.display.set_mode((conf["window_width"], conf["window_height"]))

while quit_game == False:
    
    #We display the title screen
    playerChoice = display.displayTitleScreen(conf, window)

    #We launch the game
    if playerChoice == "1":

        #At launch, we display the first level
        quit_game = display.displayLevel(1, window)

    else:
        quit_game = True

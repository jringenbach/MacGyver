#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

import pygame
from pygame.locals import *

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
                print("A key has been pressed.")

            elif event.type == QUIT:
                print("Goodbye!")
                continuer = False

    return playerChoice
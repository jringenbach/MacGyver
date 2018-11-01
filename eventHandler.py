#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

#python modules
import pygame
from pygame.locals import *


def titleScreenKeydown(event):
    """Handle the keydown event during the title screen"""
    
    continuer = True

    #The player choses to play a new game
    if event.key == K_KP1:
        continuer = False

    return continuer
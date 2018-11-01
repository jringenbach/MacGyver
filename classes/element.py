#! /usr/bin/env python3
# coding: utf-8

import path

class element:
    """Element of the game : player, guardian, needle etc...
    
    Attributes:
    :name: Name of the element
    :csvSymbol: Symbol that represents the element in the csv file
    :skin: path to the png image
    :blockThePlayer: Boolean : True if the element blocks the player, False otherwise."""

    def __init__(self, name, csvSymbol, blockThePlayer):
        self.name = name
        self.csvSymbol = csvSymbol
        self._skin = None
        self._set_skin()
        self.blockThePlayer = blockThePlayer

    def _get_skin(self):
        """Getters for the path of the skin"""

        return self._skin

    def _set_skin(self):
        """Set the path for the skin to be displayed for this element"""
        fileName = self.name+"png"
        self._skin = path.setPath("resources/img", fileName)

    skin = property(_get_skin, _set_skin)
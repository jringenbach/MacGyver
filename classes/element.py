#! /usr/bin/env python3
# coding: utf-8


# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------


import json
import path

class Element:
    """Element of the game : player, guardian, needle etc...
    
    Attributes:
    :name: Name of the element
    :csvSymbol: Symbol that represents the element in the csv file
    :skin: path to the png image
    :blockThePlayer: Boolean : True if the element blocks the player, False otherwise."""

    def __init__(self, name, blockThePlayer):
        self.name = name

        self._csvSymbol = None
        self._set_CSV_symbol()

        self._skin = None
        self._set_skin()
        
        self.blockThePlayer = blockThePlayer


# ----------------------------------------------------------------
#                      GETTERS AND SETTERS
# ----------------------------------------------------------------



    def _get_skin(self):
        """Getters for the path of the skin"""

        return self._skin



    def _set_skin(self):
        """Set the path for the skin to be displayed for this element"""
        fileName = self.name+".png"
        self._skin = path.setPath("resources/img", fileName)



    def _get_CSV_symbol(self):
        """Get the csv symbol of the element"""
        return self._csvSymbol



    def _set_CSV_symbol(self):
        """Set the csv symbol of the element"""

        #We set the path to the json file that contains the correspondence table between name of an element and its symbol
        symbolDictPath = path.setPath("resources", "element.json")

        try:
            jsonDict = open(symbolDictPath)
            print(type(jsonDict))
        except:
            print("Couldn't open the element.json file in Element._set_CSV_symbol()")

        json_str = jsonDict.read() 

        symbolDict = json.loads(json_str) #Convert the string json into a dict

        self._csvSymbol = symbolDict[self.name]


    skin = property(_get_skin, _set_skin)
    csvSymbol = property(_get_CSV_symbol, _set_CSV_symbol)
#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

import json
import os

# ----------------------------------------------------------------
#                           METHODS
# ----------------------------------------------------------------

def json_to_dictionary(directoryfile, jsonName):
    """Open a json file and set its datas in a dictionary"""

    #We set the path where we'll get the title screen image
    directoryproject = os.path.dirname(__file__)
    filePath = os.path.join(directoryproject, directoryfile, jsonName)

    #We open the json file
    jsonFile = open(filePath)
    data = json.load(jsonFile)

    return data

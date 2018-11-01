#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

import os

# ----------------------------------------------------------------
#                           METHODS
# ----------------------------------------------------------------

def setPath(pathFolder, file_name):
    """Set the path for a file and returns it as a string"""

    directory = os.path.dirname(__file__)
    file_path = os.path.join(directory, pathFolder, file_name)


    return file_path
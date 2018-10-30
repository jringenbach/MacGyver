#! /usr/bin/env python3
# coding: utf-8

# ----------------------------------------------------------------
#                           IMPORT
# ----------------------------------------------------------------

import os

# ----------------------------------------------------------------
#                           METHODS
# ----------------------------------------------------------------

def setTitleScreenPath(title_screen_name):
    """Set the path where the title screen is """

    directory = os.path.dirname(__file__)
    title_screen_path = os.path.join(directory, "resources/img", title_screen_name)

    print("Title Screen Path : "+title_screen_path)

    return title_screen_path
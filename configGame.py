#! /usr/bin/env python3
# coding: utf-8

import path

def setConfiguration(config_dict):
    """Set all the configuration of the game """

    config_dict["title_screen_path"] = path.setTitleScreenPath("title_screen.png")

    return config_dict
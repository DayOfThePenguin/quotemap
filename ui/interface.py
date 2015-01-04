#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Requires Python 3
"""
The module contains the user interface functions for quotemap
"""
#    Copyright (C) 2014-2015 by
#    Colin Dablain <colin.dablain@gmail.com>
#    All rights reserved.
#    Licensed under GNU GPL v3; see license.txt

from utilities.console import getTerminalSize

def getChoice(options):
    """
    Prints an array of options to the screen and prompts the
    user to choose one

    PARAMETERS
    ----------
    options : array of choices that the user has to choose from

    RETURNS
    -------
    The index of the user's choice in the options array

    NOTES
    -----
    This module uses Python 3's input style.
    """
    (width, height) = getTerminalSize()
    ## Print options ##
    num = 1
    for option in options:
        print("%i. %s" % (num, option))
        num += 1
    ## Print newlines between bottom of options and selection line ##
    returns = height - num - 1
    num = 0
    while (num < returns):
        print()
        num += 1
    ## Selection ##
    choice = int(input("Selection: "))
    return(choice - 1)## the list position is one greater than the index ##

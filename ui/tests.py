#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Requires Python 3
"""
Tests ui functions
"""
#    Copyright (C) 2014-2015 by
#    Colin Dablain <colin.dablain@gmail.com>
#    All rights reserved.
#    Licensed under GNU GPL v3; see license.txt

import unittest
import interface

class UITest(unittest.TestCase):
    def setUp(self):
        self.options = ["one", "two", "three"]

    def test_choose(self):
        interface.getChoice(self.options)

if __name__ == '__main__':
    unittest.main()

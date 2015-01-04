#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Requires Python 3
"""
This is the main script of quotemap; from it you can store quotes
from books (and other media).
"""
#    Copyright (C) 2014-2015 by
#    Colin Dablain <colin.dablain@gmail.com>
#    All rights reserved.
#    Licensed under GNU GPL v3; see license.txt

from datatypes import quote as q
from datatypes import book as b

from datatypes.book import Book
from datatypes.quote import Quote

from utilities.io import make_json_serializable
from ui import interface

__author__ = "Colin Dablain <colin.dablain@gmail.com>"

#nq = Quote(2, "asdf", "asdf")
#nb = Book({"title": "Test Book", "author": "Test author"})

interface.getChoice(b.attributes)





#
#options = ['Create New Book', 'Load Existing Book']
#
#
#def startNewBook():
#    """Prompts the user to input the data required to instantiate
#        a Book object
#
#
#        Notes
#        _____
#
#        The first section (until the while loop) gets the basic
#        information required to describe the book.  The second
#        section prompts the user to add additional data that will be
#        appended to the dictionary of metadata
#...."""
#
#    # First section
#
#    system('clear')
#    metadata = {}
#    print('Enter the following data as prompted')
#    metadata['title'] = raw_input('\tTitle: ')
#    metadata['author'] = raw_input('\tAuthor: ')
#    metadata['year'] = raw_input('\tYear: ')
#    system('clear')
#    print('You will now be prompted to enter additional metadata\nabout '
#           + metadata['title']
#          + ' in the form of key-value pairs. When\nyou are done, '
#          + 'press return.')
#
#    # Second section
#
#    c = 1
#    while True:
#        print('\nMeta Property ' + str(c) + ':')
#        key = raw_input('\tKey: ')
#        if key == '':
#            break
#        metadata[key] = raw_input('\tValue: ')
#        c += 1
#
#    # Third section
#
#    return Book(metadata)
#
#
#def loadBook():
#
#    filename = raw_input('Enter a title to search for: ') + '.json'
#    if rw.exists(filename):
#        json_data = rw.load(filename)
#        return Book(json_data['metadata'], json_data['quotes'])
#    else:
#        print('ERROR: \t' + filename + ' could not be loaded')
#        return 0
#
#
##                          #
##                          #
##  Start non-function code #
##                          #
##                          #
#
#system('clear')
#
## directory = '/Users/Colin/' + raw_input('Directory: /Users/Colin/')
#
#chdir('/Users/Colin/Developer/Python/QuoteMap/Quotes')
#
#b = object()
#while True:
#    print('Select one of the following options:')
#    c = 0
#    while c < len(options):
#        print('\t' + str(c + 1) + '. ' + options[c])
#        c += 1
#
#    choice = raw_input('Selection: ')
#    if choice == '1':
#        b = startNewBook()
#        break
#    if choice == '2':
#        b = loadBook()
#    if b != 0:
#        break
#
#while True:
#    system('clear')
#    print('Enter the following data about the quote.  Press\nreturn to stop '
#           + 'entering quotes')
#
#    page = ''
#    try:
#        page = input('The quote occurs on page: ')
#    except SyntaxError:
#        break
#    data = raw_input('The quote is: ')
#    comment = raw_input('My thoughts are: ')
#    b.addQuote(Quote(page, data, comment))
#    b.writeData()
#

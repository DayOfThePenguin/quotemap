#!/usr/bin/python
# -*- coding: utf-8 -*-

# Is not currently compatible with python 3, but will change input soon

from __future__ import print_function
from os import system, chdir
import json

from book import Book
from quote import Quote
import json_readwrite as rw

options = ['Create New Book', 'Load Existing Book']


def startNewBook():
    """Prompts the user to input the data required to instantiate
        a Book object


        Notes
        _____

        The first section (until the while loop) gets the basic
        information required to describe the book.  The second
        section prompts the user to add additional data that will be
        appended to the dictionary of metadata
...."""

    # First section

    system('clear')
    metadata = {}
    print('Enter the following data as prompted')
    metadata['title'] = raw_input('\tTitle: ')
    metadata['author'] = raw_input('\tAuthor: ')
    metadata['year'] = raw_input('\tYear: ')
    system('clear')
    print('You will now be prompted to enter additional metadata\nabout '
           + metadata['title']
          + ' in the form of key-value pairs. When\nyou are done, '
          + 'press return.')

    # Second section

    c = 1
    while True:
        print('\nMeta Property ' + str(c) + ':')
        key = raw_input('\tKey: ')
        if key == '':
            break
        metadata[key] = raw_input('\tValue: ')
        c += 1

    # Third section

    return Book(metadata)


def loadBook():

    filename = raw_input('Enter a title to search for: ') + '.json'
    if rw.exists(filename):
        json_data = rw.load(filename)
        return Book(json_data['metadata'], json_data['quotes'])
    else:
        print('ERROR: \t' + filename + ' could not be loaded')
        return 0


#                          #
#                          #
#  Start non-function code #
#                          #
#                          #

system('clear')

# directory = '/Users/Colin/' + raw_input('Directory: /Users/Colin/')

chdir('/Users/Colin/Developer/Python/QuoteMap/Quotes')

b = object()
while True:
    print('Select one of the following options:')
    c = 0
    while c < len(options):
        print('\t' + str(c + 1) + '. ' + options[c])
        c += 1

    choice = raw_input('Selection: ')
    if choice == '1':
        b = startNewBook()
        break
    if choice == '2':
        b = loadBook()
    if b != 0:
        break

while True:
    system('clear')
    print('Enter the following data about the quote.  Press\nreturn to stop '
           + 'entering quotes')

    page = ''
    try:
        page = input('The quote occurs on page: ')
    except SyntaxError:
        break
    data = raw_input('The quote is: ')
    comment = raw_input('My thoughts are: ')
    b.addQuote(Quote(page, data, comment))
    b.writeData()


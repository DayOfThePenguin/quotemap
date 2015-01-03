#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json_readwrite as rw


class Book(object):

    """Class for describing a book"""

    def __init__(self, metadata, quotes=[]):
        """Initializes a Book with its title, author, publication year,
         and any additional metadata the user wants to provide in the
         format specified below

         Parameters
         ----------

         metadata  :  dictionary of attirbutes of the book, including
         title, author, and publication year


         Examples
         ________

         >>> B = Book({})
      """

        self.metadata = metadata
        self.quotes = quotes

    def addQuote(self, quote):
        self.quotes.append(quote)

    def printData(self):
        print(self.metadata)
        print(self.quotes)

    def writeData(self):
        jsonData = {'quotes': self.serializeQuotes(),
                    'metadata': self.metadata}

#      print(jsonData)
#      print(self.metadata['title'])

        rw.write(self.metadata['title'], jsonData)

#      print

    def serializeQuotes(self):
        jsonQuotes = []
        for quote in self.quotes:
            jsonQuotes.append(quote.__dict__)
        return jsonQuotes

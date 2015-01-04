# -*- coding: utf-8 -*-

from __future__ import print_function
# import json_readwrite as rw

attributes = ["title", "author", "year"]

class Book(object):

    """Class for describing a book"""

    def __init__(self, metadata, quotes=[]):
        """
        Initializes a Book with its title, author, publication year,
        and any additional metadata the user wants to provide in the
        format specified below

        Parameters
        ----------

        metadata  :  dictionary of attirbutes of the book, including
        title, author, publication year (the base attributes specified
        above in attributes), and any additional key-value pairs
        the user chooses to add during input

        quotes : array of Quote objects describing quotes from the
        book. It will not be included in the constructor if the
        Book bring created has no existing data file associated with
        if

        Examples
        --------

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

    def serializeQuotes(self):
        jsonQuotes = []
        for quote in self.quotes:
            jsonQuotes.append(quote.__dict__)
        return jsonQuotes

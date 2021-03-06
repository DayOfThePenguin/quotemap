#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function
import json


class Quote(object):

    """Class for describing a quote"""

    def __init__(
            self,
            page,
            data,
            comment,
            ):
        """Initializes a Quote & describes some basic things about it

         Parameters
         ----------

         page  :  the page number the quote is from
         data  :  the quote itself
         comment  :  any comment the user has on the content of the quote
      """

        self.page = page
        self.data = data
        self.comment = comment

if (__name__ == "__main__"):
    q = Quote(12, 'hello', 'asdfasdfasdf')
    print(json.dumps(q.__dict__))
    print(q.__dict__)

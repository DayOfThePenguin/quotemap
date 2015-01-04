#!/usr/bin/python
# -*- coding: utf-8 -*-
import json


def load(name):
    f = open(name)
    print f
    data = json.load(f)
    f.close()
    return data


def write(name, data):
    filename = name + '.json'
    f = open(filename, 'w')
    json.dump(data, f)
    f.close()


def exists(name):
    try:
        open(name)
    except IOError:
        return False
    else:
        return True



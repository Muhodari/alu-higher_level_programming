#!/usr/bin/python3
'''A function to return the list of attributes and methods'''


def lookup(obj):
    '''returns the list of attributes and methods of an object'''
    return list(dir(obj))

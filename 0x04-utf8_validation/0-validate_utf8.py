#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """ method that determines if a given data set
    represents a valid UTF-8 encoding """
    acc = 0
    for b in data:
        binary = bin(b).replace('0b', '').rjust(8, '0')[-8:]
        if acc == 0:
            if binary.startswith('110'):
                acc = 1
            if binary.startswith('1110'):
                acc = 2
            if binary.startswith('11110'):
                acc = 3
            if binary.startswith('10'):
                return False
        else:
            if not binary.startswith('10'):
                return False
            acc -= 1

    return acc == 0

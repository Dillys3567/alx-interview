#!/usr/bin/python3
"""
Script to check for valid UTF-8 encodeing
"""

def validUTF8(data):
    """Return true if data is valid UTF-8 encoding, else return False"""
    i = 0
    while i < len(data):
        n = checkMSBs(data[i])
        k = i + n - (n != 0)
        i += 1
        if n == 1 or n > 4 or k >= len(data):
            return False
        while i < len(data) and i <= k:
            otherMSBs = checkMSBs(data[i])
            if otherMSBs != 1: return False
            i += 1
        return True



def checkMSBs(num):
    """Check number of leading 1s"""
    mask = 1 << (7)
    i = 0
    while num & mask:
        mask >>= 1
        i += 1
    return i
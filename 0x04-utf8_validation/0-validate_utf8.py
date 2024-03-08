#!/usr/bin/python3
"""
Script to check for valid UTF-8 encodeing
"""

def validUTF8(data):
    isUTF8 = False
    """Return true if data is valid UTF-8 encoding, else return False"""
    new_data = [convertToBinary(x) for x in data]
    n = len(new_data)
    if new_data[0][0] == '0':
        isUTF8 = True
    return isUTF8
    
    
    




def convertToBinary(number):
    """Convert a number to binary and retain only 8 LSB"""
    return (format(number,'08b'))


#!/usr/bin/python3
"""
Script to check for valid UTF-8 encodeing
"""

def validUTF8(data):
    """Return true if data is valid UTF-8 encoding, else return False"""
    new_data = [convertToBinary(x) for x in data]
    #n = len(new_data)
    if new_data[0][0] == '0':
        return True
    else:
        n = check(new_data[0])
        length = len(new_data)
        if n != (length - 1):
            return False
        for i in range(1,length -1):
            x = check(new_data[i])
            if x != 1:
                return False
    return True
    
def check(num):
    i = 0
    mask = 10000000
    num = int(num)
    while mask & num:
        mask >>=1
        i+=1
    return i

    




def convertToBinary(number):
    """Convert a number to binary and retain only 8 LSB"""
    return (format(number,'08b'))


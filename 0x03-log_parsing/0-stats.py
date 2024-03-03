#!/usr/bin/python3
"""Script to read from stdin line by line and computer metrics"""
import sys

def printMetrics(dic, size):
    """Print information"""
    print("File size: {:d}".format(size))
    for code in sorted(dic.keys()):
        if dic[code] != 0:
            print("{}: {:d}".format(code, dic[code]))


codes = {"200":0, "301":0,"400" :0, "401":0, "403":0, "404":0, "405":0, "500":0}


count = 0
size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
           printMetrics(codes,size)

        input = line.split()
        count += 1

        try:
            size += int(input[-1])
        except:
            pass

        try:
            if input[-2] in codes:
                codes[input[-2]] += 1
        except:
            pass
    printMetrics(codes,size)


except KeyboardInterrupt:
    printMetrics(codes,size)
    raise



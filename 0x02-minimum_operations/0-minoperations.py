#!/usr/bin/python3
"""
calculate the fewest number of
operations needed to result in exactly n H 
characters in the file given number n
"""

def primeNumbersInRange(n):
    """
    Finds prime numbers between 1 and n
    """
    primes = [2]
    for i in range(1,n+1):
        for j in range(2, i):
            if (i % j == 0) and (j is not i):
                break
            elif i not in primes:
                primes.append(i)
    return(primes)




def minOperations(n):
    """
    Method that calculates the fewest number of 
    operations needed to result in exactly n H 
    characters in the file
    """
    primes = primeNumbersInRange(n)


    print()

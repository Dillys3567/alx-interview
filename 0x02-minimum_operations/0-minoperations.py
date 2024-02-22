#!/usr/bin/python3
"""
calculate the fewest number of
operations needed to result in exactly n H 
characters in the file given number n
"""

def primeFactors(n):
    """
    Finds prime factors
    """
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
    return factors
 


def minOperations(n):
    """
    Method that calculates the fewest number of 
    operations needed to result in exactly n H 
    characters in the file
    """
    if (n < 0):
        return 0
    factors = primeFactors(n)
    return sum(factors)
    

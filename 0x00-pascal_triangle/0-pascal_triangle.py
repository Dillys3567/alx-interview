#!/usr/bin/python3

from math import factorial

"""
Returns a list of integers of Pascal's triangle
"""

def pascal_triangle(n):
	"""
	Return list of integers
	"""
	f = factorial
	triangle = []
	if (n == 0):
		return triangle
	else:
		for i in range(n):
			row = []
			for j in range(i + 1):
				row.append(f(i) // f(j) // f(i-j))
			triangle.append(row)
	return triangle

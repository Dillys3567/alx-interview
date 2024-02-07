#!/usr/bin/python3

from math import factorial
"""
Returns a list of integers of Pascal's triangle
"""

def pascal_triangle(n):
	f = factorial
	triangle = []
	"""
	Return list of integers
	"""
	if (n == 0):
		return []
	else:
		for i in range(n):
			row = []
			for j in range(i + 1):
				row.append(f(i) // f(j) // f(i-j))
			triangle.append(row)
	return triangle

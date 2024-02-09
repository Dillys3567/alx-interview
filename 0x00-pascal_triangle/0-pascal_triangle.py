#!/usr/bin/python3

"""
Returns a list of integers of Pascal's triangle
"""

def factorial(n):
	"""
 	Find the factorial of a number
  	"""
	if (n == 0):
		return 1
	fact = 1
	for i in range(1, n+1):
		fact*=i
	return fact
		       
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

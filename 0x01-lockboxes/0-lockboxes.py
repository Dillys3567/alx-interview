#!/usr/bin/python3
"""
Given a number of locked boxes each numbered rom 0 to n - 1
Determine if a box can be opened
"""

def canUnlockAll(boxes):
	"""
	Return True if all boxes can be opened, else return False
	"""
	keys = [0]
	for key in keys:
		for boxK in boxes[key]:
			if (boxK not in keys and boxK < len(boxes)):
				keys.append(boxK)
	if (len(keys) == len(boxes)):
		return True
	else:
		return False

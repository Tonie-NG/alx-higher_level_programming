#!/usr/bin/python3
"""Defines a function that adds two numbers."""

def add_integer(a, b=98):
	"""Return the sum of its arguments.

	Floats are typecasted to integers before addition.

	Raises:
		TypeError: If either of its arguments is not a valid integer or float.
	"""

	if (not isinstance(a, int) and not isinstance(a, float)):
		raise TypeError("a must be an integer")
	if (not isinstance(b, int) and not isinstance(b, float)):
		raise TypeError("b must be an integer")
	return (int(a) + int(b))

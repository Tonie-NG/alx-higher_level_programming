#!/usr/bin/python3

if __name__ == "__main__":
	from calculator_1 import add, sub, div, mul
	from sys import argv, exit

	operators = ['+', '-', '*', '/']
	no_of_args = len(argv) - 1
	if no_of_args != 3:
		print("Usage: ./100-my_calculator.py <a> <operator> <b>")
		exit(1)
	elif argv[2] not in operators:
		print("Unknown operator. Available operators: +, -, * and /")
		exit(1)
	else:
		a = int(argv[1])
		b = int(argv[3])
		operator = argv[2]
		if operator == '*':
			print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
		if operator == '+':
			print("{} {} {} = {}".format(a, operator, b, add(a, b)))
		if operator == '-':
			print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
		if operator == '/':
			print("{} {} {} = {}".format(a, operator, b, div(a, b)))

#!/usr/bin/python3

if __name__ == "__main__":
    a = 1
    b = 2
    c = __import__( "add_0").add(a, b)
    print("{} + {} = {}".format(a, b, c))

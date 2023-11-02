#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    no_of_args = len(argv) - 1
    if no_of_args == 0:
        print("{} arguments".format(no_of_args))
    else:
        if no_of_args == 1:
            print("{} argument".format(no_of_args))
        else:
            print("{} arguments".format(no_of_args))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))

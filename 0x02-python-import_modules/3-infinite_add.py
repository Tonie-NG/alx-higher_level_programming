#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    no_of_args = len(argv) - 1
    if no_of_args == 0:
        print("{}".format(no_of_args))
    elif no_of_args == 1:
        print("{}".format(argv[no_of_args]))
    else:
        c = argv[1]
        for i in range(2, len(argv)):
            c += int(argv[i])
        print("{}".format(c))

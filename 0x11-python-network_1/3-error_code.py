#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    import sys
    from urllib import request, error

    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)

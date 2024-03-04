#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""


if __name__ == "__main__":
    import sys
    from urllib import parse, request

    url = sys.argv[1]
    params = {"email": sys.argv[2]}
    data = parse.urlencode(params).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as res:
        print(res.read().decode("utf-8"))

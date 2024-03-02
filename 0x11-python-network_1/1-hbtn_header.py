#!/usr/bin/python3
# sends a request to a URL and displays the value of the X-Request-Id variable

if __name__ == "__main__":
    import sys
    from urllib import request

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        print(dict(res.headers).get("X-Request-Id"))

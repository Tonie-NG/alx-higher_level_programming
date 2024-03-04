#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    req = requests.get("https://intranet.hbtn.io/status")
    res = req.text
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))

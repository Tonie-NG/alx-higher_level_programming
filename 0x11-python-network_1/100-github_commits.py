#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


if __name__ == "__main__":
    import sys
    import requests

    giturl = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1]
        )
    req = requests.get(giturl)
    jsonlist = req.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                jsonlist[i].get("sha"),
                jsonlist[i].get("commit").get("author").get("name")))
    except IndexError:
        pass

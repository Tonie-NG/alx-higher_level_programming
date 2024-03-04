#!/usr/bin/python3
""" takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == "__main__":
    from requests import get, auth
    import sys

    res = get(
            "https://api.github.com/user",
            auth=auth.HTTPBasicAuth(sys.argv[1], sys.argv[2])
            )
    print(res.json().get('id'))

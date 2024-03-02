#!/usr/bin/python3
# sends a POST request to http://0.0.0.0:5000/search_user with the letter as a paramete


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = 'http://0.0.0.0:i5000/search_user'
    params = {"q": letter}
    req = requests.post(url, data=params)

    try:
        data = req.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

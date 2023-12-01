#!/usr/bin/python3
"""6. POST an email #1"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    value = sys.argv[2]
    r = requests.post(url, data={'email': value})
    print(r.text)

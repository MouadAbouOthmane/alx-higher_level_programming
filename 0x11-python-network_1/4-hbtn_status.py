#!/usr/bin/python3
"""4. What's my status? #1"""

if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type:", type(r))
    print("\t- content:", r)

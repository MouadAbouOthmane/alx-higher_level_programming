#!/usr/bin/python3
"""0. What's my status? #0"""

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')\
            as response:
        res = response.read()
    print("Body response:")
    print("\t- type:", type(res))
    print("\t- content:", res)
    print("\t- utf8 content:", res.decode('utf-8'))

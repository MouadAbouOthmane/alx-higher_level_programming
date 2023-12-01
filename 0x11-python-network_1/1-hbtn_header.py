#!/usr/bin/python3
"""1. Response header value #0"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header = response.headers._headers
        print(next(i[1] for i in header if i[0] == 'X-Request-Id'))

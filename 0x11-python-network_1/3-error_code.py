#!/usr/bin/python3
"""3. Error code #0"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    # req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)

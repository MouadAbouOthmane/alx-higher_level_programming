#!/usr/bin/python3
"""8. Search API"""

if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    arg = sys.argv[1] if len(sys.argv) == 2 else ""
    r = requests.post(url, data={'q': arg})
    # try:
    g = r.json()
    if g == '{}':
        print('No result')
    else:
        print(g.text)
    # except Exception:
    #     print("Not a valid JSON")
    # if r.status_code == requests.codes.ok:
    #     print(r.text)
    # else:
    #     print('Error code:', r.status_code)

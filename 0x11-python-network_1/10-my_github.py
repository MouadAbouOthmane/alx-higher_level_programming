#!/usr/bin/python3
"""9. My GitHub!"""

if __name__ == "__main__":
    import requests
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': f"Bearer {password}",
        }
    url = f"https://api.github.com/users/{username}"
    r = requests.get(url).json()
    print(r['id'])

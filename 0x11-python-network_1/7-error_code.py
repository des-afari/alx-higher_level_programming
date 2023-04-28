#!/usr/bin/python3
"""
    Error code
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = argv[1]
    req = get(url)
    if req.status_code >= 400:
        print('Error code: {}'.format(req.status_code))
    else:
        print(req.text)

#!/usr/bin/python3
"""
    Error code
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    try:
        response = get(argv[1])
        # override defualt handling of exceptions and reraise them
        response.raise_for_status()
    except:
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)

#!/usr/bin/python3
"""
    Response header value #0
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    with request.urlopen(argv[1]) as response:
        print(response.getheader('X-Request-Id'))

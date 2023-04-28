#!/usr/bin/python3
"""
    Response header value #1
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    response = request.get(argv[1])
    print(response.headers.get('x-request-id'))

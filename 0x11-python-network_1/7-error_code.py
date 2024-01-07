#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and displays
the body of the response using requests package.
"""
import requests
import sys


if __name__ == "__main__":
    data = requests.get(sys.argv[1])
    if data.status_code < 400:
        print(data.text)
    else:
        print(f'Error code: {data.status_code}')

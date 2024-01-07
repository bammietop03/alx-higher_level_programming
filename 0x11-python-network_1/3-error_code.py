#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8).
"""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            data = response.read().decode('utf-8')
            print(data)
    except HTTPError as e:
        print('Error code: {}'.format(e.code))

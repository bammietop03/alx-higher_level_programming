#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    response = request.get('https://alx-intranet.hbtn.io/status')
    data = response.text
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- contnent: {}".format(data))

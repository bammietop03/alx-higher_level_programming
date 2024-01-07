#!/usr/bin/python3
"""
 Python script that takes 2 arguments in order to solve this challenge.
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = requests.get(f'https://api.github.com/repos/{argv[2]}/{argv[1]}'
                     '/commits')
    if data.status_code == 200:
        for commit in data.json()[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")

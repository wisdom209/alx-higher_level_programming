#!/usr/bin/python3
"""Get your github id"""
import sys
import requests
if __name__ == '__main__':
    """Gets the github id"""
    user = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(user, password))
    print(response.json().get('id'))

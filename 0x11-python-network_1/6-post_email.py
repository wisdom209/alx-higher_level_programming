#!/usr/bin/python3
""" Post request with requests"""
import requests
import sys

if __name__ == "__main__":
    """check post request"""
    url = sys.argv[1]
    email = sys.argv[2]
    value = {"email": email}
    response = requests.post(url, value)
    print(response.text)

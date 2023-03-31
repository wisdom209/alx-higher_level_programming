#!/usr/bin/python3
"Make a post request"
import sys
import requests
if __name__ == '__main__':
    """Implementing post request"""
    q = ""
    url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1 and sys.argv[1].isalpha() is not False:
        q = sys.argv[1]
    data = {"q": q}
    response = requests.post(url, data)
    try:
        if (response.json() and len(response.json()) > 0):
            result = response.json()
            id = result.get('id')
            name = result.get('name')
            print(f"[{id}] {name}")
        elif len(response.json()) == 0:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

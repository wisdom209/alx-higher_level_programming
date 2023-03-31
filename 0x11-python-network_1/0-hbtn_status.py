#!/usr/bin/python3
"""module to implement GET with urllib"""
import urllib.request

url = 'https://alx-intranet.hbtn.io/status'
request = urllib.request.Request
if __name__ == '__main__':
    """run the code"""
    with urllib.request.urlopen(request(url)) as response:
        content = response.read()
        print("Body response:")
        print(f"	- type: {type(content)}")
        print(f"	- content: {content}")
        if 'utf-8' in response.info().get('Content-Type'):
            print(f"	- utf8 content: OK")

#!/usr/bin/python3
""" fetches a url using urllib """
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    data = response.read()
    content = data.decode('utf-8')

print("Body response:")
print("\t- type:", type(data))
print("\t- content:", data)
print("\t- utf8 content:", content)

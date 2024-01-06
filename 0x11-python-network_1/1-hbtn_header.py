#!/usr/bin/python3
"""
Takes a url, sends a request to the url and
displays value of a response variable
"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    if 'X-Request-Id' in response.headers:
        x_request_id = response.headers['X-Request-Id']
        print(x_request_id)
    else:
        print("Header 'X-Request-Id' not found")

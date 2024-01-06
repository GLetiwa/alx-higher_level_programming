#!/usr/bin/python3
"""
Takes a url, sends a request to the url and
displays value of a response variable
"""
import urllib.request
import sys

if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

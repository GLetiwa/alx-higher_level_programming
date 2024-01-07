#!/usr/bin/python3
""" takes in a URL and an email address
sends a POST request to the passed URL with the email as a
parameter,and displays the body of the response """

import urllib.requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = urllib.request.Request(url)
    with urllib.request.urlopen(r) as response:
        print(dict(response.headers).get('X-Request-Id'))

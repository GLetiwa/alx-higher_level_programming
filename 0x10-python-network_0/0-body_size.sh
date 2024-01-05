#!/bin/bash
# Display the size of the response body in bytes for a given URL

curl -s "$1" | wc -c

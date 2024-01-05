#!/bin/bash
# Display the size of the response body in bytes for a given URL
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2

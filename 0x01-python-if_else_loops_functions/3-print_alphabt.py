#!/usr/bin/python3
for value in range(97, 123):
    if chr(value) not in ['q', 'e']:
        print(f"{chr(value)}", end="")
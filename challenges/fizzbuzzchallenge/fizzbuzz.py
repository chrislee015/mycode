#!/usr/bin/env python3

numbers_file = open("numfile.txt", "r")

## display file to the screen - .read()
print(numbers_file.read())

## close file
numbers_file.close()

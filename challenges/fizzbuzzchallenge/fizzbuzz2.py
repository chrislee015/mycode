#!/usr/bin/env python3
## create file object in "r"ead mode
with open("numfile.txt", "r") as numbersfile:
    ## readlines() creates a list by reading target
    ## file line by line
    numbers_list = numbersfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(numbers_list)

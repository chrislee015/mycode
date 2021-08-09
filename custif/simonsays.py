#!/usr/bin/env python3
import time
import random

print("Welcome to Simon Says Game")
print("Simon will show a series of X's and O'x for a brief time")
print("You will then be asked to recall the series shown")
count = 1;
current_simon_command = "X"
play = True

def main():
    while play == True:
        print("Round: {count}")
        print(current_simon_command)
        time.sleep(2.5)
        printWhiteSpace()
        user = input("What did Simon say?")
        if current_simon_command == user:
            count += 1
            current_simon_command += getNextChar()
            print("Correct! Next Round will begin soon")
            time.sleep(2)
        else:
            print("Wrong Simon did not say this")
            ans = input("Would you like to play again Yes or No")
            if ans == "yes":
                count = 1;
                current_simon_command = "X"
            else:
                play = False


def printWhiteSpace():
    print(" " * 5000)

def getNextChar():
    val = random.random()
    if  val < 0.5:
        return "O"
    else:
        return "X"

if __name__ == "__main__":
    main()

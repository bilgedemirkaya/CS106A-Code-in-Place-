"""
File: khansole_academy.py
-------------------------
Add your comments here.
"""

import random

MIN_RANDOM = 10
MAX_RANDOM = 99


def main():
    first_row()


def first_row():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    answer = int(input())
    total = num1 + num2
    while answer != total:
        print("Incorrect. The expected answer is " + str(total))
        num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
        num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        answer = int(input())
        total = num1 + num2
    if answer == total:
        print("Correct! You've gotten 1 correct in a row.")
        second_row()




def second_row():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    answer = int(input())
    total = num1 + num2

    if answer != total:
        print("Incorrect. The expected answer is " + str(total))
        first_row()

    if answer == total:
        print("Correct! You've gotten 2 correct in a row.")
        third_row()


def third_row():
    num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
    num2 = random.randint(MIN_RANDOM, MAX_RANDOM)
    print("What is " + str(num1) + " + " + str(num2) + "?")
    answer = int(input())
    total = num1 + num2

    if answer != total:
        print("Incorrect. The expected answer is " + str(total))
        first_row()
    if answer == total:
        print("Correct! You've gotten 3 correct in a row.")
        print("Congratulations! You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

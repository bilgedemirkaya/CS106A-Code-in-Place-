"""
File: nimm.py
-------------------------
It is a game which has two players, each player takes a stone either 1 or 2 times at a time. Player who takes the last stone loses.
"""


def main():
    num_stones = 20
    usertrack = 1

    while num_stones > 0:
        print("There are " + str(num_stones) + " stones left")
        answer = int(input("Player " + str(usertrack) + " would you like to remove 1 or 2 stones? "))

        while answer != 1 and answer != 2:
            answer = int(input("Please enter 1 or 2: "))

        print("")
        num_stones = num_stones - answer
        if usertrack == 2:
            usertrack -= 1
        else:
            usertrack = 1
            usertrack += 1

    print("Player " + str(usertrack) + " wins!+63")


if __name__ == '__main__':
    main()

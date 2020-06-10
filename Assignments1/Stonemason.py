from karel.stanfordkarel import *

def main():
    first_shot()
    for i in range(3):
        final_shot()

def move_and_put():
    if front_is_blocked():
        put_beeper()
    while front_is_clear():
        if beepers_present():
            move()
        else:
            put_beeper()
    if no_beepers_present():
        put_beeper()
def move_back():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def move_to_next():
    move()
    move()
    move()
    move()

def first_shot():
    turn_left()
    move_and_put()
    turn_around()
    move_back()

def final_shot():
    turn_left()
    move_to_next()
    turn_left()
    move_and_put()
    turn_around()
    move_back()


if __name__ == "__main__":
    run_karel_program()

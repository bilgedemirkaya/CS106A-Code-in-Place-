from karel.stanfordkarel import *

def main():
    for i in range(2):
        finish_one()
    for i in range(2):
        final_step()
    move_to_end()
def finish_one():
        move_to_end()
        turn_left()
        move()

def second():
    move_to_end()
    turn_right()

def final_step():
    second()
    finish_one()
    finish_one()

def move_to_end():
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()

import random
import time


def display_intro():
    print("""You are in a land inhabited by dragons.
In front you see two caves. In one of them is a friendly dragon,
who is ready to share his treasures with you. 
In the second gready and hungry dragon thet will eat you up in no time\n""")


def choose_cave():
    cave = ""
    while cave != "1" and cave != "2":
        cave = input("Which cave will you enter?\npress key 1 or 2 ")

    return cave


def check_cave(chosen_cave):
    print("You are approaching a cave...")
    time.sleep(2)
    print("It's darkness makes you tremble with fear...")
    time.sleep(2)
    print("A big dragon jumps out in front of you! It opens it`s mouth and...\n")
    time.sleep(2)

    friendly_cave = random.randint(1, 2)

    if chosen_cave == str(friendly_cave):
        print("...sharing his treasures with you!")
    else:
        print("...instantly eats you up!")


play_again = "+"

while play_again == "+":
    display_intro()
    check_cave(choose_cave())

    play_again = input("Try your luck again? (+ or -")
else:
    print("Bye!")

import random

my_name = input("Hi! What's your name?\n")

number = random.randint(1, 20)

print(f"Well, {my_name}, I guessed a number from 1 to 20")

for guasses_taken in range(6):
    print("Try to guess.")
    guess = int(input())
    if guess < number:
        print("Your number is too low.")
    elif guess > number:
        print("Your number is too big")
    else:
        print(f"Good, {my_name}! You did it in {guasses_taken} attempts")
        break
else:
    print(f"You lose. I made a {number}")

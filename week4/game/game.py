import random
import sys

# Loop until level is a positive integer
while True:
    level = input("Level: ")
    if level.isdigit():
        if int(level) >= 1:
            break

# Generate an int between 1 and level inclusive w/ random module
num = random.randint(1, int(level))

# Prompt user to guess; if not positive int -> prompt again
while True:
    while True:
        guess = input("Guess: ")
        if guess.isdigit():
            break
    guess = int(guess)

    # Response:
    # if guess is too small output Too small!
    if guess < num:
        print("Too small!")
    # if guess is too large output Too large!
    elif guess > num:
        print("Too large!")
    # if guess is equal output Just right! and exit
    else:
        print("Just right!")
        sys.exit()

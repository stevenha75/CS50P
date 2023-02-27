# import libraries
import random


def main():
    score = 0
    counter = 1
    level = get_level()

    # randomly generate 10 math problems formatted
    # as X + Y =
    for _ in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        print(num1, "+", num2, "=", end="")

        # Prompt user to answer. If answer is incorrect then output EEE
        # Reprompt a maximum of 3 times
        while True:
            ans = int(input(" "))
            if ans != num1 + num2:
                if counter == 3:
                    # Output correct answer after failing
                    print("EEE")
                    print(num1, "+", num2, "=", num1 + num2, end="\n")
                    break
                counter += 1
                print("EEE")
            else:
                counter = 1
                score += 1
                break
            print(num1, "+", num2, "=", end="")

    # Output score out of 10
    print("Score", score)


# Prompt the user for level (returns variable n)
# if user does not input 1, 2, or 3 -> prompt again
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level == 1 or level == 2 or level == 3:
            return level


def generate_integer(level):
    # raises a ValueError if level is not 1, 2, or 3:
    if level != 1 and level != 2 and level != 3:
        raise ValueError
    else:
        # returns a randomly generated non-negative integer with level digits
        if level == 1:
            return random.randint(0, 9)
        if level == 2:
            return random.randint(10, 99)
        if level == 3:
            return random.randint(100, 999)


# Conditional ensures main does not run when it is imported
if __name__ == "__main__":
    main()

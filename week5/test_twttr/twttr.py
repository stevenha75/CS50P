# To do:
# Fix spacing issue

def main():
    word = input("Input: ")
    print("Output:", shorten(word))


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_word = ""
    for i in range(len(word)):
        if word[i].lower() not in vowels:
            new_word += word[i]
    return new_word


if __name__ == "__main__":
    main()

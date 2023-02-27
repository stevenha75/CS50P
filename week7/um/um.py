import re


def main():
    print(count(input("Text: ")))


# Counts the number of times um shows up alone and returns the count
def count(s):
    return len(re.findall(r"\b *[^a-z0-9]*um[^a-z0-9]* *\b", s, re.IGNORECASE))


if __name__ == "__main__":
    main()

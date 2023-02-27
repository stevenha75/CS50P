from datetime import date
import sys
import re
import inflect


p = inflect.engine()


def main():
    DOB = input("Date of Birth: ")
    year, month, day = check_DOB(DOB)
    print(convert(int(year), int(month), int(day)))


# Check for a valid DOB
def check_DOB(DOB):
    if re.search(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$", DOB):
        return DOB.split("-")
    else:
        sys.exit("Invalid DOB")


# Convert DOB into number of days alive up to today w/ date library operations
def convert(year, month, day):
    DOB = date(year, month, day)
    current_date = date.today()
    delta_time = current_date - DOB
    total_minutes = (delta_time.days * 24) * 60
    return p.number_to_words(total_minutes, andword="").capitalize() + " minutes"


if __name__ == "__main__":
    main()

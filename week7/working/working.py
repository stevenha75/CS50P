import re


def main():
    print(convert(input("Hours: ")))


# Expects str in 12-hr format and returns 24-hr format
# Raises ValueError if format is incorrect or time is invalid (e.g., 12:60 AM)
def convert(s):
    # Finds matches for the following format: 9 AM to 5 PM or 9:00 AM to 5:00 PM
    if matches := re.search(
        r"^([1-9][0-2]?(?:\:[0-5][0-9])?(?: AM| PM)) to ([1-9][0-2]?(?:\:[0-5][0-9])?(?: AM| PM))$",
        s,
    ):
        return (
            reformat_time(matches.group(1)) + " to " + reformat_time(matches.group(2))
        )
    else:
        raise ValueError


def reformat_time(s):
    # Split the AM & PM from the time itself
    time, am_pm = s.split(" ")

    # Check for minutes and reassign variables
    if ":" in time:
        hour, minutes = time.split(":")
        hour = int(hour)
        minutes = int(minutes)
    else:
        hour = int(time)
        minutes = 0

    # Check for invalid times (error checking)
    if minutes >= 60:
        raise ValueError
    if hour > 12:
        raise ValueError

    # Conversions (PM Case)
    if am_pm == "PM":
        if hour != 12:
            hour += 12
    # AM Case
    else:
        if hour == 12:
            hour = 0

    return f"{hour:02}:{minutes:02}"


if __name__ == "__main__":
    main()

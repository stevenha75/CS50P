def main():
    fraction = input("Fraction: ")
    print(guage(convert(fraction)))


def convert(frac):
    num, den = frac.split("/")
    if int(den) == 0:
        raise ZeroDivisionError
    if num.isnumeric() and den.isnumeric() and not (int(num) > int(den)):
        return round((int(num) / int(den)) * 100)
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()

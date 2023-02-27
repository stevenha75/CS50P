# Prompt user and handle necessary exceptions
while True:
    try:
        frac = input("Fraction: ")
        num, den = frac.split('/')
        percentage = round((int(num)/int(den))*100)
    except (ZeroDivisionError, ValueError):
        pass
    else:
        if percentage <= 100:
            break

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")


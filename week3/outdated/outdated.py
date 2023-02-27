# Import Python month list
valid_months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Prompt in month-day-year order (ex. 9/8/1636 or September 8, 1646)
while True:
    date = input("Date: ")
    try:
        month, day, year = date.split(sep='/')
        # Validating each variable in case 1
        if int(month) <= 12 and int(day) <= 31 and 1 <= int(year) <= 9999:
            # Output in YYYY-MM-DD format
            print(f"{int(year):04}-{int(month):02}-{int(day):02}")
            break
    # ValueError represents the second case for the date
    except ValueError:
        try:
            month_day, year = date.split(sep=',')
            month, day = month_day.split(sep=' ')
            day = int(day.rstrip(','))
            # validating each variable
            if month in valid_months and day <= 31 and 1 <= int(year) <= 9999:
                # Output in YYYY-MM-DD format
                print(f"{int(year):04}-{valid_months.index(month)+1:02}-{int(day):02}")
                break
        except ValueError:
            pass
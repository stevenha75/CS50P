def main():
    x= (input("What time is it? "))
    hours = convert(x)
    #if statement for breakfast & prints "x time"
    if 7 <= hours <=8:
        print("breakfast time")
    #conditional for lunch & prints "x time"
    elif 12 <= hours <= 13:
        print("lunch time")
    #conditional for dinner & prints "x time"
    elif 18 <= hours <= 19:
        print("dinner time")

def convert(time):
    x,y = time.split(":")
    x= float(x)
    y= float(y)
    hours = x+(y/60)
    return hours2

if __name__ == "__main__":
    main()
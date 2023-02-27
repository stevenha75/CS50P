start_due= 50

print("Amount due:", start_due)
while True:
    # Loops until correct coin is inserted then proceeds to remove from total
    while True:
        ins = int(input("Insert Coin: "))
        if ins==25 or ins==10 or ins==5:
            start_due -= ins
            if start_due<=0:
                print("Change owed:", abs(start_due))
            else:
                print("Amount Due:", start_due)
            break
        else:
            print("Amount Due:", start_due)
    # Ends outer loop if nothing is due
    if start_due <= 0:
        break




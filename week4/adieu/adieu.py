import inflect

# Empty name list
names = []

p = inflect.engine()

try:
    while True:
        names.append(input("Name: "))
except EOFError:
    print("Adieu, adieu, to", end=" ")
    print(p.join(names))


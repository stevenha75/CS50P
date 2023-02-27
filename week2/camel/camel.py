# Takes input in camelCase and returns output in snake_Case

i = input("camelCase: ")

# Iterates through each character. Len counts the characters and returns numbers starting @ 0

print("snake_Case: ", end='')

for index in range(len(i)):
    if i[index:index+1].islower():
        print(i[index:index+1], end='')
    else:
        #if upper print _ then continue printing each character normally
        print("_", end='')
        print(i[index:index+1].lower(), end='')
print("")


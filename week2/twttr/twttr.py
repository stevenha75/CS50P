# List of vowels to exclude
list = ["a", "e", "i", "o", "u"]

input = input("Input: ")
print("Output: ", end='')

for index in range(len(input)):
    if input[index:index+1].lower() not in list:
        print(input[index:index+1], end='')
print("")
#Last print moves cursor down one

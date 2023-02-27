input= input("Expression: ")

x, y , z = input.split(" ")
x= float(x)
z= float(z)

if y == "/":
    output = x/z
elif y == "+":
    output = x+z
elif y == "-":
    output = x-z
elif y == "*":
    output = x*z

print(round(output, 1))

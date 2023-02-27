x=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Have to use equality w/ conditionals so it outputs a boolean
if x.strip()=="42" or x.lower().strip()=="forty-two" or x.lower().strip()=="forty two":
    print("Yes")
else:
    print("No")
# Empty dict
grocery_list = {}

# Infinite Loop
while True:
    try:
        item = input().upper()
        if item in grocery_list:
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
    except EOFError:
        # print items in alphabetical order w/ quantity
        for key in sorted(grocery_list.keys()):
            print(f"{grocery_list[key]} {key}")
        break
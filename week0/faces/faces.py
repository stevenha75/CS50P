def convert(x):
    y = str(x)
    new = y.replace(":)","🙂")
    final = new.replace(":(", "🙁")
    return final

def main():
    d = input()
    print(convert(d))

main()

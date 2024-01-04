x = "global"

def jasio():
    x = x * 2
    jasio()
print(x)


x = "global"

def jasio():
    x = x * 2

    print(x)
jasio()

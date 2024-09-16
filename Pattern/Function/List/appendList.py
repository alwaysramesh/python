a = []

i = 1
while i<=5:
    x = int (input("Enter number : "))
    if x in a:
        print("Value exixt ")
        pass
    else:
        a.append(x)
        i=i+1

    print(a)
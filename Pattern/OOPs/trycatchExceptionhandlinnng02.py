
a=int(input("Enter Number"))
b=int(input("Enter Number"))

try:
    c=a/b
    print(c)
except:
    print("Divide by 0 error")
else:
    print("This is calling else")
finally:
    print("BYe Bye")
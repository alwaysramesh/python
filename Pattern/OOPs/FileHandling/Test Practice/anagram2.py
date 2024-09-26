a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))

x=a*b

while a!=b:
    if a>b:
        a=a-b
    if b>a:
        b=b-a
l=x/a

print("LCM of a and b is:",l)
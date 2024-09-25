n=int(input("Enter a number:"))
a=0
b=1
if n<=0:
    print("Please enter postitive number")
else:
    print("Fabonaccie series:")
    for _ in range(n):
        print(a,end=" ")
        a=b
        b=a+b
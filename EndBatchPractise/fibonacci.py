n=int(input("enter a number"))
a,b=0,1
if n<=0:
    print("Please enter a positive integer:")
else:
    print("Fibonacci series:")
    for _ in range(n):
        print(a,end="")
        a,b=b,a+b
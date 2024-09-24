n=int(input("Enter a number"))

for i in range(1,n):
    if n%2==0:
        for j in range(1,i+1):
           print(chr(j+96),end=" ")
    if n%2==1:
        for j in range(1,i+1):
            print(chr(j+64),end="")
    print()

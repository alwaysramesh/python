n=int(input("Enter n "))
for i in range(1,n+1):
    for s in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,(2*i)):
        print("*",end=" ")
    print()
n= int(input("Enter number"))

for i in range(1,n+1):
    for s in range(1,(n-i)+1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()
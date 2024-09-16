n = int (input("Enter number:"))
mid = (n+1)/2
for i in range(1,n+1):
    for j in range(i,n+1):
        if(i==1 or i==n or j==1 or j==n or i==mid or j==mid):
            print(i, end=" ")
        else:
            print(" ", end=" ")

    print()
    

n = int(input("Enter n : "))
mid = (n+1)/2
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i==mid and j>=mid) or (i==mid and j<=mid) or (j==mid and j>=mid) or (j==mid and j<=mid)):
            print("* ",end=" ")
        else:
            print(" ",end=" ")
    print()
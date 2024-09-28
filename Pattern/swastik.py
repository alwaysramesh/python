n = 9
m = (n+1)//2
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==m or j==m or (i==1 and j>m) or (i==n and j<m) or (j==1 and i<m) or (j==n and i>m):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()
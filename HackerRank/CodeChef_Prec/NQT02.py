#sum of pairs equal to k in an
t=int(input())
for i in range(0,t,1):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(0,t,1):
        for j in range(i+1,n,1):
            if(arr[i]+arr[j]%2==0):
               count=count+1
    print(count)

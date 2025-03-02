t=int(input())
for _ in range(0,t,1):
    n=int(input())
    arr=list(map(int,input().split()))
    ecount=0
    ocount=0
    for i in range(0,n,1):
        if arr[i]%2==0:
            ecount=ecount+1
        else:
            ocount=ocount+1
    epairs=(ecount*(ecount-1))//2
    opairs=(ocount*(ocount-1))//2
    print(epairs+opairs)

a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

r = min(a,b)

while(1):
    if(r%a==0 and r%b==0):
        print("LCM",r)
        break
    r+=1

t =2
while(1):
    if(a%t==0 and b%t==0):
        print("HCF",t)
        break
    t+=1



import random

x = random.randint(1000,9999)



print(x)
n=int(input("Enter a your no.:"))
print(n)
c=x-n
if(c>0):
    print("your number big: ",c)
elif(c<0):
    print("your number small:",c)

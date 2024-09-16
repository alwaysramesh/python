import random
x=random.randint(1000,9999)
print(x)
n=int(input("Enter n: "))
print(n)
c=x-n
if(c>0):
    print("big")
elif(c<0):
    print("small")
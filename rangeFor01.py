import math 
for i in range(100,200):
 cod = 0
t = i
while(t>0):
    cod+=1
    t = t//10

t = i
sum =0

while(t>0):
    r = t%10
    sum = sum + pow(r,cod)
    t = t//10


if(i==sum):
    print("Number is armstrong",)
else:
    print("Number is not armstrong",)
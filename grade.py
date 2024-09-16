p=int(input("Enter the number pysics:"))
c=int(input("Enter the number Chemistry:"))
m=int(input("Enter the number math:"))
total =p+c+m
per=total/3
print(per)
if(per<30):
    print("Result is: Fail")
else:
    print("result is: Pass")
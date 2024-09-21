p=int(input("Enter marks Pysics:"))
c=int(input("Enter marks Chemistry:"))
m=int(input("Enter marks Math:"))

total=p+c+m
per=total/3
if per>80 and per<=100:
    print("A+")
elif per>60 and per>=80:
    print("A")
elif per>40 and per>=60:
    print("C+")
elif per>=40:
    print("Fail")
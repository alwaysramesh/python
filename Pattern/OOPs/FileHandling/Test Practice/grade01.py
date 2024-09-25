p=int(input("Enter marks of physics"))
c=int(input("Enter marks of chemistry"))
m=int(input("Enter marks of math"))

total=p+c+m
per=total/3

if per >30 and per<100:
    print("A+")
if per>60 and per<=80:
    print("A")
if per>40 and per<=60:
    print("C+")
elif per<=40:
    print("Fail")
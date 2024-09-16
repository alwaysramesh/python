'''WAP to print grade of student 
i) 100-81 A+
ii) 70-61 A 
iii) 50-41 B+
iv)40-35 C 
v) 34-0  fail 
'''
pr=float(input("Enter a percrntaage: "))
if(pr<=100 and pr>=81):
    print("your grade is: A+ ")
if(pr<=70 and pr>=61):
    print("your grade is: A")
if(pr<=50 and pr>=41):
    print("your grade is: B+")
if(pr<=40 and pr>=35):
    print("your grade is: C")
if(pr<=34 and pr>=0):
    print("You have fail")

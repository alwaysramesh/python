emp=str(input("enter emp is Female Or Male:"))
age=int(input("Enter emp age:"))

if emp=='m':
   if age>=90:
      print("Your pantioon is: 4000")
   if age>=60:
      print("your pantion is: 6000")
   elif age<60:
      print("pantion is 0")

else:
    if emp=='f':
     if age>=90:
      print("Your pantioon is: 3000")
     if age<=60 and age>=89 :
      print("your pantion is: 5000")
     elif age<60:
      print("pantion is 0")
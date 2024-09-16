'''WAP to take speed of molecule or object from user and check
 is moleculr is motion or not'''
speed = int(input("Enter a number: "))
if(speed<=5):
    print("that molecule is motion")
    
elif(speed==0):
    print("molecule is stable")
else:
    print("very high speed")
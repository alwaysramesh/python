berth=int(input("Enter your seat number:"))

berth=berth%8
if   berth==1 and berth==4:
    print("Your seat Lower")
elif berth==2 and berth==5 :
    print("Middle")
elif berth==3 and berth==6 :
    print("Upper")
elif berth==7 :
    print("Side Lower")
elif berth==0:
    print("Side Upper")
elif berth>=73 :
    print("Invalid seat")
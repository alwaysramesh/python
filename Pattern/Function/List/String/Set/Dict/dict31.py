# s={1:'Ramesh',2:'Ram'}
# a=s.clear()
# print(a)

# original={1:'Ramesh',2:'Ram'}
# # # new=original.copy()
# # print('new:',new)
# print('original:',original)

# set default
# =======================================================
# car={"Maruti":"Ciaz","Hyundai":"Verna","Hona":"Amaze"}
# print(car)
# value=car.setdefault("Hyundai")
# print("Value is",value)
# print(car)

# value=car.setdefault("Hyundai","i10")
# print("Value is",value)

# print(car)
# value=car.setdefault("Renault")
# print("Value is",value)
# print(car)
# value=car.setdefault("Audi","Q7")
# print("Value is",value)
# print(car)
# ============================================

car={"Maruti":"Ciaz","Hyundai":"Verna","Honada":"Amaze"}
newcar={k: len(v) for(k,v) in car.items()}
newsorted={k:sorted(v) for(k,v) in car.items()}
print(newcar)

print(newsorted)
# wap to accept a string from the user and print the frequency count it's
# letter i/e how many times each letter is occuring int he string:- kitte bar kon sa letter aaya hai
# =============================================
dict1={'a':1,'b':2,'c':3, 'd':4}
dict2={k:v*2 for (k,v) in dict1.items() if v>2}
print(dict2) 
#==================================
dict1={'a':1,'b':2,'c':3, 'd':4, 'e':5}
dict2={k:v*2 for (k,v) in dict1.items() if v>2 if v%2==1}
print(dict2) 

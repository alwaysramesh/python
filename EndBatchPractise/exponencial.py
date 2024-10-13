x=float(input("Enter the value x:"))
n_term=int(input("Enter the number e^x:"))
e_x=1
facorial=1
for n in range(1,n_term):
    facorial=facorial*n
    e_x=e_x+(x**n)/facorial
    print("Aproximation of e^x",x,"using",n_term,"terms:",e_x)
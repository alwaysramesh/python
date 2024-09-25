x = float(input("Enter the value of x: "))
n_terms = int(input("Enter the number of terms to approximate e^x: "))

e_x = 1  
fact = 1  

for n in range(1, n_terms):
    fact *= n  
    e_x += (x ** n) / fact  
print("Approximation of e^", x, "using", n_terms, "terms:", e_x)


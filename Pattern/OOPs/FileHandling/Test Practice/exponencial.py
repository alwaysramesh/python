# Input for x and the number of terms to use in the series
x = float(input("Enter the value of x: "))
n_terms = int(input("Enter the number of terms to approximate e^x: "))

# Initialize variables
e_x = 1  # Start with the first term (which is 1)
factorial = 1  # Variable to store the factorial

# Calculate e^x using the series expansion
for n in range(1, n_terms):
    factorial *= n  # Calculate factorial of n
    e_x += (x ** n) / factorial  # Add the next term to the sum

# Output the result
print("Approximation of e^", x, "using", n_terms, "terms:", e_x)


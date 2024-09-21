# Input for the number of terms
n = int(input("Enter the number of terms: "))

# Initializing the first two numbers of the Fibonacci series
a, b = 0, 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b  # Update a and b for the next iteration

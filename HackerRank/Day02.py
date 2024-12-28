'''Task
Given an integer, , perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of  6to 20, print Weird
If n is even and greater than 20 , print Not Weird'''
n = int(input().strip())

if n % 2 == 1:  # Odd numbers
    print("Weird")
elif 2 < n < 5:  # Even and in the range 2-5
    print("Not Weird")
elif 6 <= n <= 20:  # Even and in the range 6-20
    print("Weird")
else:  # Even and greater than 20
    print("Not Weird")
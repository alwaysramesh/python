# Size of the butterfly pattern
n = 6  # You can adjust this value for a larger or smaller butterfly

# Upper part of the butterfly
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, (2 * (n - i)) + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Lower part of the butterfly
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    for j in range(1, (2 * (n - i)) + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()

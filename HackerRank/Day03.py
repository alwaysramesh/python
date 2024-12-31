x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Use nested loops to generate the coordinates
result = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:  # Check the condition
                result.append([i, j, k])  # Add the combination to the result list

print(result)

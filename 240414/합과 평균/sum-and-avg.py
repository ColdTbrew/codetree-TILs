# Read input from user and split by space
arr = input().split(' ')

# Convert the first two elements to integers
a = int(arr[0])
b = int(arr[1])

# Calculate the sum of a and b
sum_ab = a + b
avg = (a + b) / 2
# Print the sum, followed by the formatted string showing the equation
print(f"{sum_ab}",avg )
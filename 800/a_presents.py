# Read the input values
n = int(input())
nums = [int(num) for num in input().split()]

# Initialize an array to store the result
res = [0] * n

# Fill the array with the correct values
for i in range(n):
    res[nums[i] - 1] = str(i + 1)

# Print the result
print(" ".join(res))

nums = input().split()
nums = [int(num) for num in nums]

counter = 0

while nums[0] <= nums[1]:
    counter += 1
    nums[0] *= 3
    nums[1] *= 2

print(counter)
    
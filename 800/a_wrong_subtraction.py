nums = input().split()
nums = [int(num) for num in nums]


number = nums[0]
for i in range(nums[-1]):
    if number % 10 != 0:
        number -= 1
    else:
        number //= 10

print(number)
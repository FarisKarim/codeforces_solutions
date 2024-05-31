nums = input().split()

nums = [int(num) for num in nums]

k = nums[0]

for i in range(2, nums[-1] + 1):
    k += (nums[0] * i)

if nums[1] > k:
    print(0)
else:
    print(k - nums[1])

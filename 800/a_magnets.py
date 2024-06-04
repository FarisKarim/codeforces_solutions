n = int(input())

nums = [int(input()) for x in range(n)]

groups = 0

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        groups += 1
        
print(groups + 1)
    
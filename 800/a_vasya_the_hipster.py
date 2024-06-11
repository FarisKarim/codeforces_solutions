nums = list(map(int, input().split()))

remaining = max(nums) - min(nums)
total = 0
while remaining >= 2:
    total += 1
    remaining -= 2
print(min(nums), total)
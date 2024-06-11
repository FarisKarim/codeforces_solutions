n = int(input())

nums = list(map(int,input().split()))
max_value = min_value = nums[0]

total = 0
for num in nums[1:]:
    # Condition for amazing performance
    if num > max_value or num < min_value:
        total += 1
        max_value = max(max_value, num)
        min_value = min(min_value, num)
print(total)
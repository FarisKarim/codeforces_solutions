from collections import Counter

nums = input().split()
print(len(nums) - len(Counter(nums)))
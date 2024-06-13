def solve(nums):
    total, max_val = 0, max(nums)
    return sum([(max_val - num) for num in nums])

n = int(input())
nums = [num for num in list(map(int, input().split()))]

print(solve(nums))

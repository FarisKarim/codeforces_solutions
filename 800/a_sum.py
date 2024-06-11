n = int(input())

def solve_sum(nums):
    max_n = max(nums)
    nums.remove(max_n)
    if nums[0] + nums[1] == max_n:
        print("YES")
    else:
        print("NO")

nums = [list(map(int,input().split())) for i in range(n)]

for num in nums:
    solve_sum(num)
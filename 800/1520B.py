def solve(num):
    if num < 10:
        return num
    


n = int(input())
nums = [int(input()) for _ in range(n)]
for num in nums:
    print(solve(num))
    
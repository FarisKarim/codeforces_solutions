from math import sqrt

def solve(arr):
    x = int(sqrt(sum(arr)))
    if x * x == sum(arr):
        return True
    return False
    

n = int(input())
nums = [[input(), list(map(int, input().split()))] for _ in range(n)]


for x, num in nums:
    print("YES" if solve(num) else "NO")
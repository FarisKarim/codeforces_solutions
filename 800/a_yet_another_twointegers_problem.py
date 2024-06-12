from math import ceil
n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]


for x, y in nums:
    difference = abs(x - y)
    print(ceil(difference / 10))
        
    
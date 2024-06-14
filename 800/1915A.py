from collections import Counter

n = int(input())

nums = [Counter(map( int, input().split())) for _ in range(n)]

for c in nums:
    print(next(k for k,v in c.items() if c[k] == 1))
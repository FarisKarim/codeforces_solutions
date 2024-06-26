from collections import Counter

t_cases = int(input())



res = []
for c in range(t_cases):
    _, nums = input(), list(map(int,input().split()))
    count = Counter(nums)
    res.append(next((k for k, v in count.items() if v >= 3), -1))
    
for r in res:
    print(r)
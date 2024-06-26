t_cases = int(input())


res = []


for _ in range(t_cases):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    res.append("YES" if k in nums else "NO")
        
for r in res:
    print(r)
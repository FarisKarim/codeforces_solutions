n = int(input())



res = []

for _ in range(n):
    l, nums = input(), list(map(int,input().split()))
    even = sum((num for num in nums if num % 2 == 0))
    odd = sum((num for num in nums if num % 2 == 1))
    res.append("NO" if odd >= even else "YES")
    
for r in res:
    print(r)
    
from collections import Counter

n = int(input())
count = Counter("Timur")

nums = [[int(input()), input()] for _ in range(n)]

for _, string in nums:
    if Counter(string) == count:
        print("YES")
    else:
        print("NO")




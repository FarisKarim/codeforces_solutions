from collections import Counter

n = int(input())
chars=  [input() for x in range(n)]

cf = Counter("codeforces")

for char in chars:
    if char in cf:
        print("YES")
    else:
        print("NO")
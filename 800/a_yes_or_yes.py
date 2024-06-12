from collections import Counter

n = int(input())

words = [input().upper() for _ in range(n)]

for word in words:
    if word == 'YES':
        print("YES")
    else:
        print("NO")


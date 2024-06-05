from collections import Counter

n = int(input())
counter = Counter(input().lower())

if len(counter) == 26:
    print('YES')
else:
    print('NO')


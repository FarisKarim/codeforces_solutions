from collections import Counter

cals = list(map(int, input().split()))

count = Counter(map(int, input()))

total = 0
for k,v in count.items():
    total += cals[k -1] * count[k]
print(total)

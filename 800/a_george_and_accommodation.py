n = int(input())

nums = [input().split() for x in range(n)]

total = 0
for x, y in nums:
    if int(y) - int(x) > 1:
        total += 1

print(total)
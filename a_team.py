problems = int(input())
lines = [input().strip() for _ in range(problems)]

res = 0
for line in lines:
    if line.count('1') >= 2:
        res += 1
print(res)

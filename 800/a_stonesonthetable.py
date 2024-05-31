n = input()
stones = input()

res = 0
for i in range(1, len(stones)):
    if stones[i] == stones[i - 1]:
        res += 1
print(res)
n = int(input())

res = []
for x in range(n):
    nums = list(map(int, input().split()))
    counter = 0
    while nums[0] % nums[1] != 0:
        counter += 1
        nums[0] += 1
    res.append(counter)

for num in res:
    print(num)
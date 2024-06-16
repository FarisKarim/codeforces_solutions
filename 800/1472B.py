n = int(input())



res = []
for _ in range(n):
    number = int(input())
    nums = list(map(int, input().split()))
    if sum(nums) % 2 == 1:
        res.append("NO")
    elif len(nums) % 2 == 1:
        res.append("NO")
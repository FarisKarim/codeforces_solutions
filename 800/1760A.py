n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]


for arr in nums:
    print(sorted(arr)[1])

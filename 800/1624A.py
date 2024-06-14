n = int(input())

for _ in range(n):
    l = int(input())
    nums = list(map(int, input().split()))
    print(max(nums) - min(nums))
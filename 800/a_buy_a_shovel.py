nums = list(map(int, input().split()))

n = 1
while True:
    if (nums[0] * n) % 10 == nums[1] or (nums[0] * n) % 10 == 0:
        break
    n += 1
    
print(n)
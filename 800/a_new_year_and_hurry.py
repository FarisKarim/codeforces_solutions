time_until_party = 240

nums = list(map(int, input().split()))

time_for_problems = time_until_party - nums[1] 

total = 0
for i in range(1, nums[0] + 1):
    time_for_problems -= (i * 5)
    if time_for_problems >= 0:
        total += 1
        
print(total)
        
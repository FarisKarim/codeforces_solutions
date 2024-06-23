n = int(input())

nums = list(map(int, input().split()))


max_length = 1
cur_length = 1
for i in range(1, len(nums)):
    if nums[i] > nums[i - 1]:
        cur_length += 1
        max_length = max(max_length,  cur_length)
    else:
        cur_length = 1
print(max_length)
    
        
    
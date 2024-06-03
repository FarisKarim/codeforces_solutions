n = int(input())


current_num = 0
max_num = 0
for i in range(n):
    nums = input().split()
    current_num -= int(nums[0])
    current_num += int(nums[1])
    max_num = max(max_num, current_num)
    
    
print(max_num)
    
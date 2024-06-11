
nums = list(map(int,input().split()))
abc = max(nums)

nums.remove(abc)

ab, bc, ac = nums
a = abc - bc
b = abc - ac
c = abc - ab
print(a, b, c)
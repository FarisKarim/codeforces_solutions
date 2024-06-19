def solve(arr):
    n = len(arr)
    max_val = 0
    for i in range(n):
        cur_product = 1
        for j in range(n):
            if i == j:
                cur_product *= (arr[j] + 1)
            else:
                cur_product *= (arr[j])
        max_val = max(cur_product, max_val)
    return max_val
            
        
        



n = int(input())
nums = [(input(), list(map(int, input().split()))) for  _ in range(n)]

for _, arr in nums:
    print(solve(arr))
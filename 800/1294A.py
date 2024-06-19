def solve(arr):
    max_v = max(arr[:-1])
    c_needed = sum(max_v - coin for coin in arr[:-1])
    if (arr[-1] - c_needed) % 3 == 0 and arr[-1] - c_needed >= 0:
        print("YES")
    else:
        print("NO")
        
    

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for arr in nums:
    solve(arr)
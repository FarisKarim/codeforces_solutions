n = int(input())
nums = [[int(input()), list(map(int,input().split()))] for _ in range(n)]



for _, arr in nums:
    longest = 0
    cur = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            cur += 1
            longest = max(longest, cur)
            continue
        cur = 0
    print(longest)
        
        
            
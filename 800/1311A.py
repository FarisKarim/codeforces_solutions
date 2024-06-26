def solve(a, b):
    if a==b:
        return 0
    
    difference = abs(b - a)
    if a < b:
        if difference % 2 == 1:
            return 1
        else:
            return 2
    else:
        if difference % 2 == 1:
            return 2
        else:
            return 1
        
        



n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]


for a, b in nums:
    print(solve(a, b))
    
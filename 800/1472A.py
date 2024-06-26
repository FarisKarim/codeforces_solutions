t_cases = int(input())


def solve(w, h, n):
    pieces = 1
    
    while (w % 2 == 0 or h % 2 == 0) and pieces < n:
        if w % 2 == 0:
            w //= 2
            pieces *= 2
        if h % 2 == 0:
            h //= 2
            pieces *= 2
    if pieces >= n:
         return True
    return False
    
    
        


nums = [list(map(int, input().split())) for _ in range(t_cases)]


for w, h, n in nums:
    if solve(w, h, n):
        print("YES")
    else:
        print("NO")
    
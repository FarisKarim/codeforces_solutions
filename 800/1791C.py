t_cases = int(input())


cases = [[int(input()), input()] for _ in range(t_cases)]


for n, num in cases:
    l = 0
    r = n - 1
    ans = n
    while ans > 0 and num[l] != num[r]:
        l += 1
        r -= 1
        ans -= 2
    print(ans)
    
    
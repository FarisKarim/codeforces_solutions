n = int(input())


ways = 0
i = 1
while i < n:
    employees_left = n - i
    if employees_left % i == 0:
        ways += 1
    i += 1
print(ways)
        
    
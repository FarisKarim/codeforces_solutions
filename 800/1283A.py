n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]

for hour, minute in times:
    h_left = (24 - hour) * 60
    total = h_left - minute
    print(total)
    
    
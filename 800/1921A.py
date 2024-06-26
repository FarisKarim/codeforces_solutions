t_cases = int(input())


res = []

for _ in range(t_cases):
    coords = [list(map(int, input().split())) for _ in range(4)]
    x_set = []
    y_set = []
    for x, y in coords:
        if x not in x_set and len(x_set) <= 2:
            x_set.append(x)
        if y not in y_set and len(y_set) <= 2:
            y_set.append(y)
    res.append(abs(x_set[0] - x_set[1]) * abs(y_set[0] - y_set[1]))
    
for r in res:
    print(r)
    
        
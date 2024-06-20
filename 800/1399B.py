t_cases = int(input())

cases = [(int(input()), list(map(int, input().split())), list(map(int, input().split()))) for _ in range(t_cases)]

for _, candies, oranges in cases:
    total = 0
    min_c, min_o = min(candies), min(oranges)
    
    for i in range(_):
        total += max(candies[i] - min_c, oranges[i] - min_o)
    print(total)  
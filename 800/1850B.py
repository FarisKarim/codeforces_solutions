t_cases = int(input())


res = []

for _ in range(t_cases):
    n = int(input())
    winner = -1
    b_quality = 0
    for i in range(1, n + 1):
        a, b = map(int, input().split())
        if a <= 10 and b > b_quality:
            b_quality = b
            winner = i
    res.append(winner)

for w in res:
    print(w)
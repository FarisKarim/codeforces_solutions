def solve(rows):
    for row in rows:
        if any(c not in ('W', 'B', 'G') for c in row):
            return "#Color"
    return "#Black&White"



n, _ = list(map(int, input().split()))
rows = [input().split() for x in range(n)]

print(solve(rows))

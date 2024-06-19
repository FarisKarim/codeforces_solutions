def solve(s1, s2):
    s1 = s1.replace('G', 'B')
    s2 = s2.replace('G', 'B')
    return s1 == s2
            



n = int(input())
rows = [(int(input()), input(), input()) for _ in range(n)]

for row in rows:
    r1, r2 = row[1], row[2]
    if solve(r1, r2):
        print("YES")
    else:
        print("NO")
def solve(letters):
    seen = set()
    i = 0
    for i in range(1, len(letters)):
        if letters[i] in seen:
            return "NO"
        if letters[i] != letters[i - 1]:
            seen.add(letters[i - 1])
    return "YES"
        

n = int(input())

res = []
for _ in range(n):
    days, letters = int(input()), input()
    res.append(solve(letters))

for ans in res:
    print(ans)
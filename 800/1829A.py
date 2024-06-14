n = int(input())

strings = [input() for _ in range(n)]

cf = 'codeforces'


for s in strings:
    total = 0
    for i in range(len(s)):
        if s[i] != cf[i]:
            total += 1
    print(total)
    
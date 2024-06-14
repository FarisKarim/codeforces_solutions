n = int(input())

strings = [input() for x in range(n)]

for s in strings:
    res = []
    for i in range(0, len(s) - 2, 2):
        res.append(s[i:i+2])
    res.append(s[-2:])
    ans = ''
    for subs in res[:-1]:
        ans += subs[0]
    ans += res[-1]
    print(ans)
        
    
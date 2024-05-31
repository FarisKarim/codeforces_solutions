summans = input().split('+')

summans = sorted([int(x) for x in summans])

ans = ""
for i in range(len(summans) - 1):
    ans += (str(summans[i]) + "+")
ans += str(summans[-1])
print(ans)
n = int(input())

events = list(map(int, input().split()))

unnoticed = 0
police = 0
for e in events:
    if e == -1:
        if police == 0:
            unnoticed += 1
        else:
            police -= 1
    else:
        police += e

print(unnoticed)
        
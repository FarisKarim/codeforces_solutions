n = int(input())

total = 0

for i in range(n):
    poly = input()[0].lower()
    if poly == 't':
        total += 4
    elif poly == 'c':
        total += 6
    elif poly == 'o':
        total += 8
    elif poly == 'd':
        total += 12
    else:
        total += 20
print(total)
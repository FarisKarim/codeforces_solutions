n = int(input())


res = ''
for i in range(1, n  + 1):
    res += 'I '
    if i % 2 == 1:
        res += 'hate that '
    else:
        res += 'love that '
print(res[:-5] + 'it')
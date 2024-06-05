k, l, m, n, d = [int(input()) for _ in range(5)]

count = 0

for i in range(1, d + 1):
    if any(i % divisor == 0 for divisor in (k, l, m, n)):
        count += 1
print(count)
n = int(input())

bills = [100, 20, 10, 5, 1]

total= 0

for bill in bills:
    while n >= bill:
        total += 1
        n -= bill
print(total)
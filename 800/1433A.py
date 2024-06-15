n = int(input())

numbers = [(input()) for _ in range(n)]

for number in numbers:
    total = 0
    total += (int(number[0]) - 1) * 10
    for _ in range(1, len(number) + 1):
        total += _
    print(total)

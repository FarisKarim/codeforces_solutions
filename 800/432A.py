n, p_times = list(map(int, input().split()))


players = list(map(int, input().split()))

total = sum([1 for p in players if (5 - p_times) >= p]) // 3
print(total)
from collections import Counter

n = int(input())

levels = Counter([str(i) for i in range(1, n + 1)])

completed = Counter(input().split()[1:] + input().split()[1:])

if len(levels) == len(completed):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
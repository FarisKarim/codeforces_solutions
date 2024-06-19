from collections import Counter





n = int(input())

strings = [input() for _ in range(n)]


for s in strings:
    count = Counter(s)
    print('A' if count['A'] > count['B'] else 'B')
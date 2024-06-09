from collections import Counter

letters = ''

for i in range(2):
    letters += input()

pile = Counter(input())

if pile == Counter(letters):
    print('YES')
else:
    print('NO')
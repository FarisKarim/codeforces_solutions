from collections import Counter
n = input()
games = input()

win_count = Counter(games)

if win_count['A'] > win_count['D']:
    print('Anton')
elif win_count['A'] < win_count['D']:
    print('Danik')
else:
    print('Friendship')
    
from collections import Counter

def solve(letters):
    count = Counter(letters)
    if count['B'] == 1:
        return 1
    l = 0
    r = len(letters) - 1
    
    while letters[l] != 'B':
        l += 1
    while letters[r] != 'B':
        r -= 1
    return r - l + 1
    

res = []
t_cases = int(input())
for c in range(t_cases):
    n, letters = int(input()), input()
    res.append(solve(letters))
    
for r in res:
    print(r)
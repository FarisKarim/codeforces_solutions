lower = 0
upper = 0

word = input()

for char in word:
    if char.upper() == char:
        upper += 1
    else:
        lower += 1
        
if lower < upper:
    print(word.upper())
else:
    print(word.lower())
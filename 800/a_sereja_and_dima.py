n = int(input())

cards = list(map(int, input().split()))

p1 = 0
p2 = 0

# Shallow copy of array so we can remove card from it
for i in range(len(cards[:])):
    card_to_add = max(cards[0], cards[-1])
    if i % 2 == 0:
        p1 += card_to_add
    else:
        p2 += card_to_add
    cards.remove(card_to_add)
print(str(p1), str(p2))
grid = list(map(int, input().split()))

row = grid[0]
col = grid[1]

right = True

for i in range(row):
    if i % 2 == 0:
        print('#' * col)
    else:
        if right:
            print('.' * (col - 1) + '#')
            right = False
        else:
            print('#' + ('.' * (col - 1)))
            right = True
        
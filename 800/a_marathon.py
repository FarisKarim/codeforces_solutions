n = int(input())

nums = [list(map(int, input().split())) for x in range(n)]

def solve(array):
    total = 0
    sorted_n = sorted(array)
    print(len(sorted_n) - sorted_n.index(array[0]) - 1)

for array in nums:
    solve(array)    
def solve(arrays):
    for arr in arrays:
        if arr[0] + arr[1] == arr[2]:
            print("+")
        else:
            print("-")

n = int(input())
arrays = [list(map(int, input().split())) for _ in range(n)]

solve(arrays=arrays)
    
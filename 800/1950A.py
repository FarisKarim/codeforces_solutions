def solve(arr):
    if arr[0] < arr[1] < arr[2]:
        return "STAIR"
    if arr[1] > arr[0] and arr[1] > arr[2]:
        return "PEAK"
    return "NONE"



n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for arr in nums:
    print(solve(arr))
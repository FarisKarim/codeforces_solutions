def solve(arr):
    a, b, c = arr[0] + arr[2], arr[1] + arr[0], arr[2] + arr[1]
    if a >= 10 or b >= 10 or c >= 10:
        return True
    return False


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

for arr in nums:
    if solve(arr):
        print("YES")
    else:
        print("NO")
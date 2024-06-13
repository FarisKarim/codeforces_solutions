n = int(input())

nums = [input() for _ in range(n)]

def solve(left, right):
    if sum(map(int, left)) == sum(map(int, right)):
        print("YES")
    else:
        print("NO")

for arr in nums:
    solve(arr[:3], arr[3:])
    
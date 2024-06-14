
def solve(arr):
    x, y, n = arr
    while True and n >= y:
        if n % x == y:
            return n
        n -= 1


n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]




for arr in nums:
    print(solve(arr))
def solve(arr):
    m = min(arr)
    return (sum((num - m) for num in arr))


t_cases = int(input())
nums = [(input(), list(map(int, input().split()))) for _ in range(t_cases)]

for _, arr in nums:
    print(solve(arr))
    
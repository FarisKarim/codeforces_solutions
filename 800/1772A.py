def solve(expression):
    return int(expression[0]) +  int(expression[2])


t_cases = int(input())

nums = [input() for _ in range(t_cases)]

for expression in nums:
    print(solve(expression))
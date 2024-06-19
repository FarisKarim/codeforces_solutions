def no_duplicates(arr):
    return len(arr) == len(set(arr))


t_cases = int(input())
nums = [(input(), input().split()) for _ in range(t_cases)]

for _, arr in nums:
    if no_duplicates(arr):
        print("YES")
    else:
        print("NO")
def even_odd_count(arr):
    odd = sum(1 for num in arr if num % 2 == 1)
    return odd == sum(1 for num in arr if num % 2 == 0)



t_cases = int(input())
nums = [(input(), list(map(int, input().split()))) for _ in range(t_cases)]


for _, arr in nums:
    if even_odd_count(arr):
        print("YES")
    else:
        print("NO")
def solve(num):
    if num % 3 == 0:
        return num // 3, num // 3
    elif num % 3 == 1:
        return num //3 + 1, num //3
    else:
        return num // 3, num //3 + 1


n = int(input())

nums = [int(input()) for _ in range(n)]

for num in nums:
    print(" ".join(map(str, solve(num))))
import math

rolls = map(int, input().split())

num = 6 - max(rolls) + 1
z = math.gcd(num, 6)

x, y = num // z, 6 // z

print(f"{x}/{y}" )
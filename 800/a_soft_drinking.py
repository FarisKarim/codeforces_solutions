nums = list(map(int, input().split()))

n, k, l, c, d, p, nl, np = nums

total_ml = k * l
ml_toast = total_ml // nl
slices = c * d
salt= p // np


print(min(ml_toast, slices, salt) // n)

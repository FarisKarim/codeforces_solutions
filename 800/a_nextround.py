input_vals = input().split()
k = int(input_vals[-1])

arr = input().split()

arr = [int(num) for num in arr]

cutoff = arr[k - 1]

res = 0

for num in arr:
    if num >= cutoff and num > 0:
        res += 1
print(res)
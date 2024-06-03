inputs = input().split()

heights = input().split()

total = 0

for height in heights:
    if int(height) <= int(inputs[1]):
        total += 1
    else:
        total += 2
print(total)
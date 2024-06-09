n = int(input())

nums = [(input()) for x in range(n)]

for num in nums:
    total = 0
    round_numbers = []
    for i in range(len(num)):
        if num[i] != '0':
            total += 1
            round_numbers.append(int(num[i]) * (10 ** (len(num) - i - 1)))
    print(len(round_numbers))
    print(" ".join(map(str,round_numbers)))
        
            
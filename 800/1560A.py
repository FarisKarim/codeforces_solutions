n = int(input())

sequences = [int(input()) for x in range(n)]

def solve(k):
    num = 0
    count = 0
    while count < k:
        num += 1
        if num % 3 == 0 or str(num)[-1] == '3':
            continue
        count += 1
    print(num)


for sequence in sequences:
    solve(sequence)
            
        
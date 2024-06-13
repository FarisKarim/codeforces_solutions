from collections import Counter

n = int(input())

res = []
for _ in range(n):
    l = int(input())
    array = list(map(int,input().split()))
    counter =  Counter(array)
    diff_number = (next(k for k, v in counter.items() if v == 1))
    res.append(list(array).index(diff_number) + 1)
for num in res:
    print(str(num))

    
    
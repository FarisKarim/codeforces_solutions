from heapq import nlargest

n = int(input())

nums = [list(map(int, input().split())) for _ in range(n)]

for arr in nums:
    w1 = arr[0] if arr[0] > arr[1] else arr[1]
    w2 = arr[2] if arr[2] > arr[3] else arr[3]
    highest = nlargest(2, arr)
    
    if w1 in highest and w2 in highest:
        print("YES")
    else:
        print("NO")
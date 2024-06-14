n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]

mishka, chris = 0, 0

for arr in nums:
    if arr[0] > arr[1]:
        mishka += 1
    elif arr[0] < arr[1]:
        chris += 1
if mishka > chris:
    print("Mishka")
elif mishka < chris:
    print("Chris")
else:
    print("Friendship is magic!^^")
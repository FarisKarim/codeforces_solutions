x = 0

def solve(operation):
    global x
    if '+' in operation:
        x += 1
    else:
        x -= 1
number = int(input())
for _ in range(number):
    operation = input()
    solve(operation)
    
print(x)


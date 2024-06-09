n = int(input())

uniforms = [list(map(int, input().split())) for i in range(n)]

total = 0
for i in range(n):
    for j in range(n):
        if i != j:
            if uniforms[i][1] == uniforms[j][0]:
                total += 1
print(total)
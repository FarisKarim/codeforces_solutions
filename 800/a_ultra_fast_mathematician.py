first = input()
second = input()

res = ''.join(['1' if first[i] != second[i] else '0' for i in range(len(first))])
print(res)
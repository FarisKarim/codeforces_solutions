expression = input()

i = 0
res = ''

while i < len(expression):
    if expression[i] == '.':
        res += '0'
        i += 1
    elif expression[i] == '-':
        if expression[i + 1] == '-':
            res += '2'
            i += 2
        elif expression[i + 1] == '.':
            res += '1'
            i += 2
print(res)
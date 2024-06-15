def solve(string):
    if len(string) % 2 == 1:
        return "NO"
    return "YES" if string[:len(string)//2] == string[len(string)//2:] else "NO"


n = int(input())

strings = [input() for _ in range(n)]

for s in strings:
    print(solve(s))
n = int(input())

problems = [(int(input()), input()) for _ in range(n)]

for x, string in problems:
    print(2 * len(set(string)) + (1 * (len(string) - len(set(string)))))
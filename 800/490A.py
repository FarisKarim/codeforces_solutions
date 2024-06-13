n = int(input())

people = list(map(int, input().split()))

dic = {}

def solve(people):
    dic = {1: [], 2: [], 3: []}
    
    for i in range(n):
        dic[people[i]].append(i + 1)
        
    res = []
    teams = min(len(dic[1]), len(dic[2]), len(dic[3]))
    for x in range(teams):
        res.append([dic[1].pop(), dic[2].pop(), dic[3].pop()])
    
    print(teams)
    if res:
        for x in range(len(res)):
            print(" ".join(map(str, res[x])))
            
solve(people)


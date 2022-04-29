import sys
sys.setrecursionlimit(10 ** 5)
INF = int(1e9)

n = int(sys.stdin.readline())

score = []
result = [INF]
select_score = []
all_team = set([i for i in range(n)])

for _ in range(n):
    score.append(list(map(int, sys.stdin.readline().split())))

visited = [True for _ in range(n)]

def backtrack(x, start):
    if x == n // 2:
        other_score = list(all_team - set(select_score))
        minValue(select_score, other_score)

    else:
        #중복을 어찌 없애야 하나... 찾음... start를 붙여주면 되는 문제였다!
        for i in range(start, n):
            if visited[i]:
                visited[i] = False
                select_score.append(i)
                backtrack(x + 1, i+1)
                select_score.pop()
                visited[i] = True

def minValue(select_score, other_score):
    sum_score = 0
    other_team_score = 0

    for i in range(len(select_score)):
        for j in range(i+1, len(select_score)):
            sum_score += score[select_score[i]][select_score[j]] + score[select_score[j]][select_score[i]]
            other_team_score += score[other_score[i]][other_score[j]] + score[other_score[j]][other_score[i]]

    diff = abs(other_team_score - sum_score)

    if result[0] > diff:
        result[0] = diff

backtrack(0, 0)

print(result[0])
import sys

case = int(sys.stdin.readline())

for _ in range(case):
    n, k, t, m = map(int, sys.stdin.readline().split())

    team = [[] for _ in range(n+1)]
    submit = [0 for _ in range(n+1)]
    result = []
    cnt = 0

    for cnt in range(m):
        i, j, s = map(int, sys.stdin.readline().split())
        check = True

        if len(team[i]) >= 1:
            for problem in team[i]:
                if problem[0] == j:
                    check = False
                    if problem[1] < s:
                        problem[1] = s
                    problem[2] = cnt

        submit[i] += 1

        if check:
            team[i].append([j, s, cnt])

        cnt += 1

    for team_id in range(1, n + 1):
        score = 0
        last_num = 0
        for prob_num in range(len(team[team_id])):
            score += team[team_id][prob_num][1]
            if team[team_id][prob_num][2] > last_num:
                last_num = team[team_id][prob_num][2]
        result.append((team_id, score, submit[team_id], last_num))

    result.sort(key=lambda x: (-x[1], x[2], x[3]))

    for rank in range(len(result)):
        if result[rank][0] == t:
            print(rank+1)
            break

# 다른사람 풀이
# import sys
# input=sys.stdin.readline
#
# T=int(input())
# for _ in range(T):
#     n,k,t,m=map(int,input().split())
#     board=[[0]*k for _ in range(n)]
#     count=[0]*n #제출횟수
#     time=[0]*n #제출시간
#     for ts in range(m):
#         i,j,s=map(int,input().split())
#         board[i-1][j-1]=max(board[i-1][j-1],s)
#         time[i-1]=ts
#         count[i-1]+=1
#     new=[]
#     for idx in range(len(board)):
#         new.append([sum(board[idx]),count[idx],time[idx],idx])
#     new.sort(key=lambda x:(-x[0],x[1],x[2])) #규칙대로정렬
#     for idx in range(len(new)):
#         if new[idx][3]==t-1:
#             print(idx+1)
#             break
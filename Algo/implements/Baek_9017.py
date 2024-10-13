import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    players = list(map(int, sys.stdin.readline().split()))

    teams = list(set(players))
    index = 1
    score = dict()

    for team in teams:
        if players.count(team) == 6:
            score[team] = [1, 0, 0]

    keys = list(score.keys())

    for i in range(n):
        for key in keys:
            if players[i] == key:
                if score[key][0] <= 4:
                    score[key][1] += index
                elif score[key][0] == 5:
                    score[key][2] = index
                index += 1
                score[key][0] += 1

    sorted_keys = sorted(score.keys(), key=lambda k: (score[k][1], score[k][2]))

    print(sorted_keys[0])

# 다른 사람 풀이
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     count = {}  # 팀 당 주자 수
#     temp = list(map(int, input().split()))
#
#     # 팀 별로 주자 수 세기
#     for i in range(n):
#         if temp[i] in count:
#             count[temp[i]] += 1
#         else:
#             count[temp[i]] = 1
#
#     # 제외되는 팀 구하기
#     dele = {}  # 제외되는 팀
#     for k, v in count.items():
#         if v < 6:
#             dele[k] = 1
#
#     # 점수 계산
#     team = {}
#     idx = 1  # 점수
#     for i in range(n):
#         if temp[i] not in dele:
#             if temp[i] in team:
#                 if team[temp[i]][0] < 4:
#                     team[temp[i]][0] += 1
#                     team[temp[i]][1] += idx
#                 elif team[temp[i]][0] == 4:
#                     team[temp[i]][0] += 1
#                     team[temp[i]][2] = idx
#             else:
#                 team[temp[i]] = [1, idx, 0]  # [팀당 주자 수, 상위 4명 점수 합, 5번째 주자의 점수]
#
#             idx += 1
#
#     # 순위 정렬
#     team = sorted(team.items(), key=lambda x: (x[1][1], x[1][2]))
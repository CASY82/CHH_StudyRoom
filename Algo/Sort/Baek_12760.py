# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# player = []
# player_score = [0] * n
#
# for _ in range(n):
#     player.append(list(map(int, sys.stdin.readline().split())))
#
# #세로로 변환 한다음 최대값 index 추출(가 아니라 자신이 가진 카드중 제일 큰 값을 내는 거였음)
# for i in range(m):
#     card = []
#
#     for j in range(n):
#         card.append(player[j][i])
#
#     for j in range(n):
#         if card[j] == max(card):
#             player_score[j] += 1
#
#     print(card)
#     print(player_score)
#
#
#
# for i in range(len(player_score)):
#     if max(player_score) == player_score[i]:
#         print(i+1, end=' ')

import sys

n, m = map(int, sys.stdin.readline().split())
player = []
player_score = [0] * n

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.sort(reverse=True)
    player.append(tmp)

#세로로 변환 한다음 최대값 index 추출(가 아니라 자신이 가진 카드중 제일 큰 값을 내는 거였음)
for i in range(m):
    card = []

    for j in range(n):
        card.append(player[j][i])

    for j in range(n):
        if card[j] == max(card):
            player_score[j] += 1

for i in range(len(player_score)):
    if max(player_score) == player_score[i]:
        print(i+1, end=' ')
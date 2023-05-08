import sys

n = int(sys.stdin.readline())
players = []

for _ in range(n):
    players.append(list(map(int, sys.stdin.readline().split())))

score = [0 for _ in range(n)]
for case in range(3):
    tmp = [0 for _ in range(n)]
    tmp_dic = dict()
    for people in range(n):
        tmp[people] = players[people][case]
        if players[people][case] not in tmp_dic:
            tmp_dic[players[people][case]] = 1
        else:
            tmp_dic[players[people][case]] += 1

    for card in range(n):
        if tmp_dic[tmp[card]] == 1:
            score[card] += tmp[card]

for answer in score:
    print(answer)
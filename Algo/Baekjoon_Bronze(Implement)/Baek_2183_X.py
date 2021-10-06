# n, s = input().split()
# player = [chr((65 + i)) for i in range(int(n))]
# game_wins = [0 for i in range(int(n))]
# set_wins = [0 for i in range(int(n))]
# set_change = 0
#
# for i in range(len(s)):
#     game_wins[player.index(s[i])] += 1
#     before = player[player.index(s[i])]
#
#     if before != s[i]:
#         set_change = 0
#     else:
#         set_change += 1
#
#     if max(game_wins) == 6:
#         if set_change != 6:
#             set_change = 0
#             set_wins[game_wins.index(max(game_wins))] += 1
#             game_wins = [0 for i in range(int(n))]
#         else:
#             set_change = 0
#             set_wins[game_wins.index(max(game_wins))] += 2
#             game_wins = [0 for i in range(int(n))]
#
#     if max(set_wins) == 3:
#         break
#
# print(player[set_wins.index(max((set_wins)))])

#https://ipsc.ksp.sk/2005/real/solutions/a.html 문제 해결 방법에 대한 내용 참고 이 문제는 이해를 못해서 틀림
n, s = input().split()

print(s[len(s)-1])
import sys

n = int(sys.stdin.readline())
player = []

for _ in range(n):
    player_status = list(map(int, sys.stdin.readline().split()))

    player.append([player_status[0], player_status[1] * player_status[2] * player_status[3], player_status[1] + player_status[2] + player_status[3]])

player.sort(key=lambda x:(x[1], x[2], x[0]))

print(player[0][0], player[1][0], player[2][0])
import sys

n, game_name = sys.stdin.readline().strip().split()
n = int(n)

player = set()
game = {"Y": 1, "F": 2, "O": 3}

for _ in range(n):
    player.add(sys.stdin.readline().strip())

print(len(player) // game[game_name])
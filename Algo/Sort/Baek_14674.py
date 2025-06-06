import sys
from fractions import Fraction

n, k = map(int, sys.stdin.readline().split())
games = []

for _ in range(n):
    game = list(map(int, sys.stdin.readline().split()))
    gasungbi = Fraction(game[2], game[1])

    games.append([gasungbi, game[1], game[0]])

games.sort(key=lambda x:(-x[0], x[1], x[2]))

for i in range(k):
    print(games[i][2])
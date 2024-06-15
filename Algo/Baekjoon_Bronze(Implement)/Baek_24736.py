import sys

away = list(map(int, sys.stdin.readline().split()))
home = list(map(int, sys.stdin.readline().split()))

away_score = away[0] * 6 + away[1] * 3 + away[2] * 2 + away[3] + away[4] * 2
home_score = home[0] * 6 + home[1] * 3 + home[2] * 2 + home[3] + home[4] * 2

print(away_score, home_score)

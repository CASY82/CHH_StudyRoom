import sys

team1 = list(map(int, sys.stdin.readline().split()))
team2 = list(map(int, sys.stdin.readline().split()))

t1_total = team1[0] + team1[1] * 2 + team1[2] * 3
t2_total = team2[0] + team2[1] * 2 + team2[2] * 3

if t1_total > t2_total:
    print(1)
elif t1_total < t2_total:
    print(2)
else:
    print(0)
import sys

a, b, g = map(int, sys.stdin.readline().split())
team_a = set(sys.stdin.readline().strip().split())
team_b = set(sys.stdin.readline().strip().split())
goals = list(sys.stdin.readline().strip().split())

a_score = 0
b_score = 0

for i in range(g):
    if goals[i] in team_a:
        a_score += 1
    else:
        b_score += 1

if a_score > b_score:
    print("A")
elif a_score < b_score:
    print("B")
else:
    print("TIE")

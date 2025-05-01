import sys

n, p = map(int, sys.stdin.readline().split())
w, l, g = map(int, sys.stdin.readline().split())

score = 0
winner = set()
check = True

for _ in range(p):
    name, type = sys.stdin.readline().strip().split()

    if type == "W":
        winner.add(name)

for _ in range(n):
    user = sys.stdin.readline().strip()

    if user in winner:
        score += w
    else:
        if score - l <= 0:
            score = 0
        else:
            score -= l

    if score >= g:
        check = False
        print("I AM NOT IRONMAN!!")
        break

if check:
    print("I AM IRONMAN!!")
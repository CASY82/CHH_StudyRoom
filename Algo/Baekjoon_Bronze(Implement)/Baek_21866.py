import sys

score_max = [100, 100, 200, 200, 300, 300, 400, 400, 500]
score = list(map(int, sys.stdin.readline().split()))
res = ""

if sum(score) >= 100:
    res = "draw"
else:
    res = "none"

for i in range(len(score)):
    if score[i] > score_max[i]:
        res = "hacker"
        break

print(res)
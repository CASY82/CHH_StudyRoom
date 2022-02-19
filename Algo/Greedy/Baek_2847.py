import sys

n = int(sys.stdin.readline())
score = []
result = 0

for _ in range(n):
    score.append(int(sys.stdin.readline()))

for i in range(n, -1, -1):
    for j in range(i+1, n):
        if score[i] >= score[j]:
            result += score[i] - score[j] + 1
            score[i] -= score[i] - score[j] + 1

print(result)
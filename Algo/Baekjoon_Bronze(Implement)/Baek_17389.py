import sys

n = int(sys.stdin.readline())
score = list(sys.stdin.readline().strip())

result = 0
bonus = 0

for i in range(n):
    if score[i] == 'O':
        result += (i + 1) + bonus
        bonus += 1
    else:
        bonus = 0

print(result)
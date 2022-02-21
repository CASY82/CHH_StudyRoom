import sys

n, m = map(int, sys.stdin.readline().split())
apple = []
j = int(sys.stdin.readline())
result = 0
move = [(i+1) for i in range(m)]

for _ in range(j):
    apple.append(int(sys.stdin.readline()))

for i in range(len(apple)):
    if apple[i] > max(move):
        tmp = abs(apple[i] - max(move))
        result += tmp
        for k in range(len(move)):
            move[k] += tmp
    elif apple[i] < min(move):
        tmp = abs(apple[i] - min(move))
        result += tmp
        for k in range(len(move)):
            move[k] -= tmp
    else:
        continue
print(result)
import sys

n, q = map(int, sys.stdin.readline().split())

money = [0 for _ in range(n + 1)]

for _ in range(q):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == '1':
        money[int(command[1])] += int(command[2])
    else:
        print(sum(money[int(command[1]):int(command[2]) + 1]))
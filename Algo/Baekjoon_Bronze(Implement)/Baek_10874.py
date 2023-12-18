import sys

n = int(sys.stdin.readline())
test = []
correct = []

for _ in range(n):
    test.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, 11):
    correct.append(((i - 1) % 5 + 1))

for i in range(1, n + 1):
    if test[i - 1] == correct:
        print(i)
import sys

n, q = map(int, sys.stdin.readline().split())
tempo = list(map(int, sys.stdin.readline().split()))

if n < 2:
    total = []
else:
    total = [abs(tempo[1] - tempo[0])]

    for i in range(1, n - 1):
        total.append(abs(tempo[i + 1] - tempo[i]) + total[i - 1])

for _ in range(q):
    i, j = map(int, sys.stdin.readline().split())

    if i >= j:
        print(0)
    else:
        if i == 1:
            print(total[j - 2])
        else:
            print(total[j - 2] - total[i - 2])
# Grid de Largada

import sys

data = sys.stdin.read().strip().split()
it = iter(data)

while True:
    try:
        n = int(next(it))
    except StopIteration:
        break  # EOF

    start = [int(next(it)) for _ in range(n)]
    finish = [int(next(it)) for _ in range(n)]

    index = []

    for i in range(n):
        index.append(start.index(finish[i]))

    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if index[i] > index[j]:
                cnt += 1

    print(cnt)
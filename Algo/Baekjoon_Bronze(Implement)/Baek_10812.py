import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

array = [i for i in range(n+1)]

for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())

    tmp_arr = deque(array[i:j+1])

    for _ in range(k-i):
        tmp_arr.append(tmp_arr.popleft())

    loc = 0
    for num in range(i, j+1):
        array[num] = tmp_arr[loc]
        loc += 1

for result in range(1, len(array)):
    print(array[result], end=" ")
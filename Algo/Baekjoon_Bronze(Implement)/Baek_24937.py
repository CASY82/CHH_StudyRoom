import sys
from collections import deque

n = int(sys.stdin.readline())

tmp = n % 10
tmp_str = deque('SciComLove')

for i in range(n):
    front = tmp_str.popleft()
    tmp_str.append(front)

print(''.join(tmp_str))
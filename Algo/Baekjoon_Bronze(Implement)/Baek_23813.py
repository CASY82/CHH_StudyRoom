import sys
from collections import deque

num = list(sys.stdin.readline().strip())
result = 0

result += int(''.join(num))
tmp = deque(num)

for _ in range(len(num)-1):
    tmp.appendleft(tmp.pop())
    result += int(''.join(list(tmp)))

print(result)
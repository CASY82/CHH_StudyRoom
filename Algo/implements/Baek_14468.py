# 소가 길을 건너간 이유2

import sys

command = sys.stdin.readline().strip()
stack = []
seen = set()
ans = 0

for ch in command:
    if ch not in seen:
        seen.add(ch)
        stack.append(ch)
    else:
        pos = stack.index(ch)
        ans += len(stack) - pos - 1
        stack.pop(pos)

print(ans)
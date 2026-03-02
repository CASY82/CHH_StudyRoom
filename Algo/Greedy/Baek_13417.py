# 카드 문자열
import sys
from collections import deque

def prefer_front(dq: deque, x: str) -> bool:
    if not dq:
        return True

    n = len(dq)
    total = n + 1

    def getA(k: int) -> str:
        return x if k == 0 else dq[k - 1]

    def getB(k: int) -> str:
        return dq[k] if k < n else x

    for k in range(total):
        a = getA(k)
        b = getB(k)
        if a != b:
            return a < b

    return True

def solve_one(cards):
    dq = deque()
    for x in cards:
        if prefer_front(dq, x):
            dq.appendleft(x)
        else:
            dq.append(x)
    return ''.join(dq)

t = int(sys.stdin.readline())
out = []

for _ in range(t):
    n = int(sys.stdin.readline())
    words = list(sys.stdin.readline().strip().split())

    out.append(solve_one(words))

print("\n".join(out))
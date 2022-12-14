import sys
from collections import deque

n = int(sys.stdin.readline())
damage = list(map(int, sys.stdin.readline().split()))
result = True

junwon = damage[0]
damage = damage[1:]
damage.sort()

damage = deque(damage)

while damage:
    if junwon > damage[0]:
        junwon += damage[0]
        damage.popleft()
    else:
        result = False
        print("No")
        break

if result:
    print("Yes")

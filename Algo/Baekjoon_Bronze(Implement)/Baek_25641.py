import sys
from collections import deque

n = int(sys.stdin.readline())
sodduck = deque(list(sys.stdin.readline().strip()))

while True:
    if sodduck.count("s") == sodduck.count("t"):
        break

    sodduck.popleft()

print("".join(list(sodduck)))
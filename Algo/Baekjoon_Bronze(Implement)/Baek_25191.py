import sys

n = int(sys.stdin.readline())
cola, beer = map(int, sys.stdin.readline().split())

cola = cola // 2
can_chick = cola + beer

print(min(can_chick, n))
import sys

rabbit, m, k = map(int, sys.stdin.readline().split())
wolf = 0
jump = 0

while wolf < rabbit:
    wolf += k
    rabbit += m
    jump += 1

print(jump)
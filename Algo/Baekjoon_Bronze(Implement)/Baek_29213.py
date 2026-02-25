# Колевская бухгалтерия
import sys

a, b, c = map(int, sys.stdin.readline().split())

ans = 0

for x in range(c + 1):
    max_y_by_c = c - x
    max_y_by_ineq = (a + x - b - 1)
    max_y = min(max_y_by_c, max_y_by_ineq)
    if max_y >= 0:
        ans += (max_y + 1)

print(ans)
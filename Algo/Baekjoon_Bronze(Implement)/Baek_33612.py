import sys

n = int(sys.stdin.readline())

data = [[2024, 8], [2025, 3], [2025, 10], [2026, 5], [2026, 12]]

print(*data[n - 1])
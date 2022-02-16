import sys

n = int(sys.stdin.readline())

full = n - int(n * 22 / 100)
gyungbi = n - int(n * 20 / 100 * 22 / 100)
print(full, gyungbi)
import sys

n = int(sys.stdin.readline())

cells = "a b c d e f g h".split(" ")

print(cells[(n - 1) % 8] + str((n - 1) // 8 + 1))
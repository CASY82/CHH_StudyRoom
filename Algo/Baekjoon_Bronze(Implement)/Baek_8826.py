import sys

z = int(sys.stdin.readline())

direct = ['N', 'S', 'W', 'E']
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for _ in range(z):
    num = int(sys.stdin.readline())
    move = sys.stdin.readline().strip()
    x = 0
    y = 0

    for i in range(len(move)):
        x += dx[direct.index(move[i])]
        y += dy[direct.index(move[i])]

    print(abs(x) + abs(y))

# 다른사람 풀이
# import sys
#
# n = int(sys.stdin.readline())
# for i in range(n):
# 	m = int(sys.stdin.readline())
# 	ewsn = sys.stdin.readline().strip()
# 	print(abs(ewsn.count("S") - ewsn.count("N")) + abs(ewsn.count("E") - ewsn.count("W")))
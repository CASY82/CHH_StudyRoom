#input을 쓰면 시간 초과가 난다...
import sys
n = int(sys.stdin.readline())
point = []

for _ in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort(key = lambda x: (x[1], x[0]))

for i in range(len(point)):
    print(point[i][0], point[i][1])
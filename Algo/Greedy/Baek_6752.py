import sys

t = int(sys.stdin.readline())
case = int(sys.stdin.readline())
times = []

for _ in range(case):
    times.append(int(sys.stdin.readline()))

times.sort()
tmp = 0
cnt = 0

for i in range(case):
    if tmp + times[i] > t:
        break

    tmp += times[i]
    cnt += 1

print(cnt)
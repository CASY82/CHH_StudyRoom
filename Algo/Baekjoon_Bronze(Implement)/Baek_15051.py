import sys

a1 = int(sys.stdin.readline())
a2 = int(sys.stdin.readline())
a3 = int(sys.stdin.readline())

times = [0, 0, 0]

times[0] = a2 + a3 * 2
times[1] = a1 + a3
times[2] = a1 * 2 + a2

print(min(times) * 2)
import sys

problem = []
extra_total = 0

for _ in range(11):
    d, v = map(int, sys.stdin.readline().split())

    extra_total += v * 20
    problem.append(d)

problem.sort()
time = 0
total_time = 0

for i in problem:
    time += i
    total_time += time

print(total_time + extra_total)
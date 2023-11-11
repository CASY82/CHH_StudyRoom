import sys

n = int(sys.stdin.readline())
solved_problem = []

penalty = 0

for i in range(1, n + 1):
    t, s = map(int, sys.stdin.readline().split())

    solved_problem.append((t, s, i))

solved_problem.sort(key=lambda x : (-x[1], x[0]))

f = solved_problem[0][2]

if solved_problem[0][1] == 0:
    print(0)
else:
    print(solved_problem[0][0] + (f - 1) * 20)
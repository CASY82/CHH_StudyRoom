import sys

n = int(sys.stdin.readline())
problem = []

for _ in range(n):
    title, num = sys.stdin.readline().strip().split()
    num = int(num)
    problem.append([title, num])

problem.sort(key= lambda x : x[1])

print(problem[0][0])
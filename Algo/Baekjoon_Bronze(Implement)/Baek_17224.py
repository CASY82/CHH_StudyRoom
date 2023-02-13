import sys

n, l, k = map(int, sys.stdin.readline().split())
problem_list = []
result = 0

for i in range(n):
    easy, difficult = map(int, sys.stdin.readline().split())

    if difficult <= l:
        problem_list.append(140)
    elif easy <= l:
        problem_list.append(100)
    else:
        continue

problem_list.sort(reverse=True)

for i in range(k):
    if i <= len(problem_list)-1:
        result += problem_list[i]

print(result)
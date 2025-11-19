import sys

n = int(sys.stdin.readline())
students = []

for _ in range(n):
    name, score, risk, cost = sys.stdin.readline().strip().split()

    score = int(score)
    risk = int(risk)
    cost = int(cost)

    scholar = (score ** 3) // (cost * (risk + 1))

    students.append([scholar, cost, name])

students.sort(key=lambda x : (-x[0], x[1], x[2]))

print(students[1][2])
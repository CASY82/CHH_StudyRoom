import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    grade = 0
    gpa = 0

    for _ in range(n):
        c, g = sys.stdin.readline().split()

        c = int(c)
        g = float(g)

        grade += c
        gpa += g*c

    print(grade)
    print('%0.1f' % float(gpa / grade))
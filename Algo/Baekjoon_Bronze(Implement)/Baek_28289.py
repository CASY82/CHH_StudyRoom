import sys

p = int(sys.stdin.readline())

software = 0
embeded = 0
ai = 0
one_grade = 0

for _ in range(p):
    grade, ban, num = map(int, sys.stdin.readline().split())

    if grade == 1:
        one_grade += 1
    elif grade >= 2:
        if ban == 1 or ban == 2:
            software += 1
        elif ban == 3:
            embeded += 1
        elif ban == 4:
            ai += 1

print(software)
print(embeded)
print(ai)
print(one_grade)
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    name, score = sys.stdin.readline().split()
    result = ''

    score = int(score)

    if score >= 97:
        result = 'A+'
    elif score >= 90:
        result = 'A'
    elif score >= 87:
        result = 'B+'
    elif score >= 80:
        result = 'B'
    elif score >= 77:
        result = 'C+'
    elif score >= 70:
        result = 'C'
    elif score >= 67:
        result = 'D+'
    elif score >= 60:
        result = 'D'
    else:
        result = 'F'

    print(name, result)
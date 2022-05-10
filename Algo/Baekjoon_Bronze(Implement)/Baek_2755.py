import sys

n = int(sys.stdin.readline())
result = 0
total_hak = 0

for _ in range(n):
    subject, hakjum, score = sys.stdin.readline().strip().split()

    tmp = 0

    if score == "A+":
        tmp = 4.3
    elif score == "A0":
        tmp = 4.0
    elif score == "A-":
        tmp = 3.7
    elif score == "B+":
        tmp = 3.3
    elif score == "B0":
        tmp = 3.0
    elif score == "B-":
        tmp = 2.7
    elif score == "C+":
        tmp = 2.3
    elif score == "C0":
        tmp = 2.0
    elif score == "C-":
        tmp = 1.7
    elif score == "D+":
        tmp = 1.3
    elif score == "D0":
        tmp = 1.0
    elif score == "D-":
        tmp = 0.7
    else:
        tmp = 0

    result += tmp * float(hakjum)
    total_hak += int(hakjum)

def rounder(num):
    tmp = list(str(num))

    if len(tmp) > 4:
        if int(tmp[4]) >= 5:
            tmp[3] = str(int(tmp[3]) + 1)

    num = "".join(tmp[:4])

    return "%.2f" % float(num)

print(rounder(result/total_hak))
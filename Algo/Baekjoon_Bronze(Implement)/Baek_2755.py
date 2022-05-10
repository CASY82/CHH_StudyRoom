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

# 반올림을 다른사람들은 어떻게 했을까?
# import sys
#
# grade = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.3, 'B0': 3.0, 'B-': 2.7, 'C+': 2.3, 'C0': 2.0, 'C-': 1.7, 'D+': 1.3, 'D0': 1.0, 'D-': 0.7, 'F':0.0}
#
# N = int(sys.stdin.readline())
# grade_sum = 0
# grade_cnt = 0
# for _ in range(N):
#     _, g, n = sys.stdin.readline().rstrip().split()
#
#     grade_sum += int(g) * grade[n]
#     grade_cnt += int(g)
#
# print('%.2f'%(grade_sum/grade_cnt + 0.000000000001))

# import sys
#
# input = sys.stdin.readline
#
# tot = 0.0
# k = 0
# for _ in range(int(input())):
#     __, p, s = input().split()
#     p = int(p)
#     k += p
#
#     if s[0] == 'A':
#         tot += 4 * p
#     elif s[0] == 'B':
#         tot += 3 * p
#     elif s[0] == 'C':
#         tot += 2 * p
#     elif s[0] == 'D':
#         tot += p
#     if len(s) < 2:
#         pass
#     elif s[1] == '+':
#         tot += 0.3 * p
#     elif s[1] == '-':
#         tot -= 0.3 * p
#
# tot /= k
# tot = int(tot * 100 + 0.5)
#
# print('%d.%02d' % (tot // 100, tot % 100))
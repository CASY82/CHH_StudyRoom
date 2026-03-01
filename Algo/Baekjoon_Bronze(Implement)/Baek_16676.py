# 근우의 다이어리 꾸미기

import sys

salary = sys.stdin.readline().strip()

length = len(salary)
check = ""

for _ in range(len(salary)):
    check = check + "1"

check = int(check)
salary = int(salary)

if check <= salary:
    print(length)
else:
    if salary == 0:
        print(1)
    else:
        print(length - 1)
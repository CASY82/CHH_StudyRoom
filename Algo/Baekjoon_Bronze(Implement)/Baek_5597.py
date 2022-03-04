import sys

student = [True] * 30

for i in range(28):
    num = int(sys.stdin.readline())

    student[num-1] = False

for i in range(30):
    if student[i]:
        print(i+1)
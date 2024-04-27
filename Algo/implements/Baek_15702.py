import sys

n, m = map(int, sys.stdin.readline().split())

prob_score = list(map(int, sys.stdin.readline().split()))
max_student = [100001, 0]

for _ in range(m):
    student = list(sys.stdin.readline().strip().split())

    stu_score = 0

    for i in range(1, n + 1):
        if student[i] == "O":
            stu_score += prob_score[i - 1]

    if stu_score > max_student[1]:
        max_student[0] = int(student[0])
    elif stu_score == max_student[1]:
        max_student[0] = min(max_student[0], int(student[0]))

    max_student[1] = max(max_student[1], stu_score)

print(*max_student)
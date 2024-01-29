import sys

n = int(sys.stdin.readline())
student = list(sys.stdin.readline().strip().split())
result = [0 for _ in range(n)]

for _ in range(n):
    like_list = list(sys.stdin.readline().strip().split())

    for p in like_list:
        result[student.index(p)] += 1

mapped_list = list(zip(student, result))
mapped_list.sort(key=lambda x: -x[1])

for stu, cnt in mapped_list:
    print(stu, cnt)
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    g = int(sys.stdin.readline())
    student = []
    i = 1

    for _ in range(g):
        student.append(int(sys.stdin.readline()))

    if len(student) == 1:
        print(1)
    else:
        while True:
            tmp = set()
            for stu in student:
                if stu % i not in tmp:
                    tmp.add(stu % i)

            if len(tmp) == len(student):
                print(i)
                break

            i += 1
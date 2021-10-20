t = int(input())

for _ in range(t):
    blank = input()
    n = int(input())
    student = []
    for i in range(n):
        student.append(int(input()))

    result = sum(student)

    if result % n == 0:
        print('YES')
    else:
        print('NO')
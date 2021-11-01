t = int(input())

for _ in range(t):
    num = input()
    new_num = ''

    for i in range(len(num)-1, -1, -1):
        new_num += num[i]

    checker = int(new_num) + int(num)
    checker = str(checker)
    check = False

    if len(checker) % 2 == 0:
        for j in range(len(checker) // 2):
            if checker[j] == checker[len(checker) - 1 - j]:
                check = True
            else:
                check = False
    else:
        mid = len(checker) // 2
        for j in range(mid):
            if checker[j] == checker[len(checker) - 1 - j]:
                check = True
            else:
                check = False

    if check == True:
        print('YES')
    else:
        print('NO')
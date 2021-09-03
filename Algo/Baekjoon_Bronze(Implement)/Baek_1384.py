group = 1

while True:
    student = []
    people = int(input())
    word = [[] for i in range(people)]
    check = 0

    if people == 0:
        break

    for i in range(people):
        student.append(list(input().split()))

    for i in range(people):
        for j in range(1, people):
            if student[i][j] == 'N':
                if i > j:
                    word[i].append(student[i - j][0] + ' was nasty about ' + student[i][0])
                elif i < j:
                    word[i].append(student[people - j + i][0] + ' was nasty about ' + student[i][0])
                else:
                    word[i].append(student[0][0] + ' was nasty about ' + student[i][0])

    print('Group '+ str(group))
    for i in range(len(word)):
        if word[i] and word[i] != '':
            for j in word[i]:
                print(j, end=' ')
            check = 1
            print()

    if check == 0:
        print('Nobody was nasty')

    print()

    group += 1


# 좀더 간단해 보이는 풀이
# group = 0
#
# while True:
#     group += 1
#     num = int(input())
#     if num == 0:
#         break
#     ms = []
#     for i in range(num):
#         ms.append(input().split())
#     idx = 0
#     clean = 0
#     print("Group", group)
#     while idx < num:
#         for i in range(1, num):
#             if ms[idx][i] == "N":
#                 clean += 1
#                 print(ms[idx - i][0], "was nasty about", ms[idx][0])
#         idx += 1
#     if clean == 0:
#         print("Nobody was nasty")
#
#     print()

# while True:
#     color = [0 for i in range(3)]
#     alpha = dict()
#
#     try:
#         checker, checked = input().split()
#     except:
#         break
#
#     alpha_set = list(set(checker))
#     for i in range(len(alpha_set)):
#         alpha.setdefault(alpha_set[i], checker.count(alpha_set[i]))
#
#     for i in range(len(checker)):
#         if checker[i] == checked[i]:
#             alpha[checker[i]] -= 1
#             color[0] += 1
#             continue
#
#     for i in range(len(checker)):
#         if checker[i] == checked[i]:
#             continue
#
#         if checked[i] in checker:
#             if alpha[checked[i]] > 0:
#                 if i > 0 and (checked[i] == checker[i - 1]):
#                     color[1] += 1
#                     alpha[checked[i]] -= 1
#                 elif i < (len(checker) - 1) and (checked[i] == checker[i + 1]):
#                     color[1] += 1
#                     alpha[checked[i]] -= 1
#                 else:
#                     color[2] += 1
#                     alpha[checked[i]] -= 1
#
#
#     print(checked, ': ', color[0], ' black, ', color[1], ' grey, ', color[2], ' white', sep='')

while True:
    color = [0 for i in range(3)]
    alpha = dict()

    try:
        checker, checked = input().split()
    except:
        break

    mapping = [True] * len(checker)
    checker = list(checker)
    checked = list(checked)

    alpha_set = list(set(checker))
    for i in range(len(alpha_set)):
        alpha.setdefault(alpha_set[i], checker.count(alpha_set[i]))

    for i in range(len(checker)):
        if checker[i] == checked[i]:
            alpha[checker[i]] -= 1
            color[0] += 1
            mapping[i] = False

    for i in range(len(checker)):
        if checker[i] == checked[i]:
            continue

        if checked[i] in checker:
            if alpha[checked[i]] > 0:
                if i > 0 and (checked[i] == checker[i - 1]) and mapping[i - 1]:
                    color[1] += 1
                    alpha[checked[i]] -= 1
                    mapping[i - 1] = False
                elif i < (len(checker) - 1) and (checked[i] == checker[i + 1]) and mapping[i + 1]:
                    color[1] += 1
                    alpha[checked[i]] -= 1
                    mapping[i + 1] = False
                else:
                    for j in range(len(checker)):
                        if checked[i] == checker[j] and mapping[j]:
                            color[2] += 1
                            alpha[checked[i]] -= 1
                            mapping[j] = False


    print(''.join(checked), ': ', color[0], ' black, ', color[1], ' grey, ', color[2], ' white', sep='')
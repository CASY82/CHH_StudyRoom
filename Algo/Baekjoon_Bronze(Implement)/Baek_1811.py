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

# 나에게 정답을 알려주신분의 코드
# from sys import stdin, stdout
#
# while 1:
#     x = stdin.readline().split()
#     if x[0] == "#":
#         break
#     target = x[0]
#     guess = x[1]
#     ans = [0, 0, 0]
#     n = len(target)
#     visit_t = [0]*n
#     visit_g = [0]*n
#     for i in range(n):
#         if target[i] == guess[i]:
#             visit_t[i] = 1
#             visit_g[i] = 1
#             ans[0] += 1
#
#     for i in range(n):
#         if visit_g[i] == 1:
#             continue
#         if i > 0 and guess[i] == target[i-1] and visit_t[i-1] == 0:
#             visit_g[i] = 1
#             visit_t[i-1] = 1
#             ans[1] += 1
#             continue
#         if i < n-1 and guess[i] == target[i+1] and visit_t[i+1] == 0:
#             visit_g[i] = 1
#             visit_t[i+1] = 1
#             ans[1] += 1
#             continue
#
#     for i in range(n):
#         if visit_t[i] == 1:
#             continue
#         for j in range(n):
#             if visit_g[j] == 1:
#                 continue
#             if target[i] == guess[j]:
#                 visit_t[i] = 1
#                 visit_g[j] = 1
#                 ans[2] += 1
#                 break
#     stdout.write(f"{guess}: {ans[0]} black, {ans[1]} grey, {ans[2]} white\n")

# from collections import*
# for i in[*open(0)][:-1]:
#     v,w=i.split();a=b=g=0;v=[*v];x=[*w];C=Counter(v)
#     for i,j in enumerate(x):
#         if v[i]==j:C[j]-=1;a+=1;v[i]=x[i]=0
#     for i in range(len(x)):
#         for j in (k for k in(i-1,i+1)if -1<k<len(x)):
#             if 0!=v[j]==x[i]:C[x[i]]-=1;v[j]=x[i]=0;g+=1
#     for i in x:
#         if C[i]:C[i]-=1;b+=1
#     print(f'{w}: {a} black, {g} grey, {b} white')
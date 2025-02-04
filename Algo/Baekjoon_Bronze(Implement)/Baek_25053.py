import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    score = [-1] * 11
    check = True

    for i in range(n):
        val, qst_num = map(int, sys.stdin.readline().split())

        score[qst_num] = max(val, score[qst_num])

    for j in range(1, 11):
        if score[j] == -1:
            print("MOREPROBLEMS")
            check = False
            break

    if check:
        print(sum(score[1:]))


# 다른 사람 풀이
# for i in range(int(input())):
#     num = int(input())
#     p = {1: -1, 2: -1, 3: -1, 4: -1, 5: -1, 6: -1, 7: -1, 8: -1, 9: -1, 10: -1}
#     for j in range(num):
#         b, d = map(int, input().split())
#         p[d] = max(p[d], b)
#     check, out = 1, 0
#     for j in range(1, 11):
#         if p[j] == -1:
#             check = 0
#         else:
#             out += p[j]
#     if check:
#         print(out)
#     else:
#         print("MOREPROBLEMS")
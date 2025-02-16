import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    n = int(sys.stdin.readline())

    if n == 0:
        res = "INSOMNIA"
    else:
        num_set = set()
        tmp = n
        res = 0
        index = 2

        while True:
            tmp_len = str(tmp)

            for i in range(len(tmp_len)):
                num_set.add(tmp_len[i])

            if len(num_set) == 10:
                res = tmp
                break

            tmp = n * index
            index += 1

    print("Case #{0}: {1}".format(case, res))

# 다른 사람 풀이
# from sys import stdin
#
# input = stdin.readline
#
# for t in range(int(input())):
#     n = int(input())
#     if n == 0:
#         print(f"Case #{t+1}: INSOMNIA")
#     else:
#         used = set()
#         nn = n
#         while True:
#             for i in str(nn):
#                 used.add(int(i))
#             if len(used) == 10:
#                 print(f"Case #{t+1}: {nn}")
#                 break
#             nn += n
import sys

while True:
    n = sys.stdin.readline().strip()
    k = 2

    if n == "":
        break

    num_cnt = [0 for _ in range(10)]

    for i in range(len(n)):
        num_cnt[int(n[i])] += 1

    tmp_n = int(n)

    while num_cnt.count(0) != 0:
        tmp = str(tmp_n * k)

        for i in range(len(tmp)):
            num_cnt[int(tmp[i])] += 1

        k += 1

    print(k-1)

# 다른 사람 풀이

# def check_list(list):
#     for x in list:
#         if not x:
#             return False
#     return True
#
# while True:
#     try:
#         n = int(input())
#         check = [0] * 10
#         k = 0
#         while True:
#             k += 1
#             s = n * k
#             ns = str(s)
#             for ch in ns:
#                 check[int(ch)] = 1
#             if check_list(check):
#                 break
#         print(k)
#     except:
#         break
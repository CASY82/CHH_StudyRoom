import sys

# 각 자리 분해해서 더한 값 리턴 함수
def digit_square(num):
    str_num = str(num)
    num_length = len(str_num)
    tmp = 0

    for i in range(num_length):
        tmp += int(str_num[i]) ** 2

    return tmp

while True:
    a, b = map(int, sys.stdin.readline().split())

    if a == b == 0:
        break

    a_arr = [a]
    b_arr = [b]
    a_tmp = a
    b_tmp = b

    while True:
        a_tmp = digit_square(a_tmp)

        if a_tmp in a_arr:
            break

        a_arr.append(a_tmp)

    while True:
        b_tmp = digit_square(b_tmp)

        if b_tmp in b_arr:
            break

        b_arr.append(b_tmp)

    result_num = 0
    result = 100000000000
    for i in range(len(a_arr)):
        if a_arr[i] in b_arr:
            tmp_arr_sum = a_arr.index(a_arr[i]) + b_arr.index(a_arr[i]) + 2
            if result > tmp_arr_sum:
                result_num = a_arr[i]
                result = tmp_arr_sum

    if result_num == 0:
        print(a, b, 0)
    else:
        print(a, b, result)

#다른 사람 풀이 참고

# import sys
#
# input = sys.stdin.readline
#
#
# def square_plus(n):
#     x = 0
#     while n > 0:
#         x += (n % 10) ** 2
#         n //= 10
#     return x
#
#
# while True:
#     a, b = map(int, input().split())
#     original_a, original_b = a, b
#     if a == 0 and b == 0:
#         break
#
#     if a == b:
#         print(a, b, 2)
#         continue
#
#     a_lst = []
#     b_lst = []
#
#     while True:
#         x = square_plus(a)
#         if x not in a_lst:
#             a_lst.append(a)
#         else:
#             a_lst.append(a)
#             break
#         a = x
#     a_set = set(a_lst)
#     cnt = 1
#     yes_break = False
#     ans_lst = []
#     while True:
#         if b in a_set:
#             for i in range(len(a_lst)):
#                 if a_lst[i] == b:
#                     ans_lst.append(i + 1 + cnt)
#
#         y = square_plus(b)
#         if y not in b_lst:
#             b_lst.append(b)
#         else:
#             b_lst.append(b)
#             break
#         b = y
#         cnt += 1
#     if ans_lst:
#         print(original_a, original_b, min(ans_lst))
#     else:
#         print(original_a, original_b, 0)
# import sys
#
# n = int(sys.stdin.readline())
#
# result = False
# first = sys.stdin.readline().strip()
# second = sys.stdin.readline().strip()
#
# first_arr = dict()
# second_arr = dict()
#
# vowels = "a,e,i,o,u".split(',')
#
# if first[0] == second[0] and first[-1] == second[-1]:
#     for i in range(n):
#         if first[i] not in first_arr:
#             first_arr[first[i]] = 1
#         else:
#             first_arr[first[i]] += 1
#
#         if second[i] not in second_arr:
#             second_arr[second[i]] = 1
#         else:
#             second_arr[second[i]] += 1
#
#     for k, v in first_arr.items():
#         if second_arr[k] != v:
#             print('NO')
#             exit()
#
#     first_exchange = first
#     second_exchange = second
#
#     for j in range(n):
#         for vow in vowels:
#             first_exchange = first_exchange.replace(vow, "")
#             second_exchange = second_exchange.replace(vow, "")
#
#     if first_exchange != second_exchange:
#         print('NO')
#         exit()
#
#     print('YES')
# else:
#     print('NO')

import sys

n = int(sys.stdin.readline())

result = False
first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

first_arr = dict()
second_arr = dict()

vowels = "a,e,i,o,u".split(',')

first_vowel = []
second_vowel = []

if first[0] == second[0] and first[-1] == second[-1]:
    first_exchange = first
    second_exchange = second

    for vow in vowels:
        first_exchange = first_exchange.replace(vow, "")
        second_exchange = second_exchange.replace(vow, "")

        first_vowel.append(first.count(vow))
        second_vowel.append(second.count(vow))

    if first_exchange != second_exchange:
        print('NO')
        exit()

    for i in range(5):
        if first_vowel[i] != second_vowel[i]:
            print('NO')
            exit()

    print('YES')
else:
    print('NO')
# n = int(input())
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in range(n):
#     dictionary = []
#     hubo = []
#     hubo_count = []
#     sascha = input()
#     exam = int(input())
#     sascha_word = list(sascha)
#
#     print(sascha_word)
#
#     for i in range(exam):
#         dictionary.append(input())
#
#     for j in dictionary:
#         count = 0
#         for k in alpha:
#             for z in sascha_word:
#                 if sascha.replace(z, k) == j:
#                     hubo.append(j)
#                     count += sascha.count(z)
#
#         if j in hubo:
#             hubo_count.append(count)
#
#     print(hubo[hubo_count.index(min(hubo_count))])

# from difflib import SequenceMatcher
#
# n = int(input())
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#
# for i in range(n):
#     dictionary = []
#     hubo = []
#     hubo_ratio = []
#     sascha = input()
#     exam = int(input())
#
#     for i in range(exam):
#         dictionary.append(input())
#
#     for j in dictionary:
#         ratio = SequenceMatcher(None, j, sascha).ratio()
#
#         if ratio > 0:
#             hubo.append(j)
#             hubo_ratio.append(ratio)
#
#     if hubo_ratio:
#         print(hubo[hubo_ratio.index(max(hubo_ratio))])
#     else:
#         print(dictionary[0])



'''
1
lolly
5
child
mommy
hello
drink
lilly

1
lolly
5
child
mommy
hello
drink
horse

1
icpc
2
risc
iupc

# 예제 입력
2
lolly
5
child
mommy
hello
drink
horse
icpc
2
risc
iupc

# 예제 출력
mommy
iupc
'''

n = int(input())
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(n):
    dictionary = []
    hubo = []
    hubo_ratio = []
    sascha = input()
    exam = int(input())

    sascha_word = list(sascha)

    for i in range(exam):
        dictionary.append(input())

    for j in dictionary:
        count = 0
        for k in alpha:
            for z in sascha_word:
                if sascha.replace(z, k) == j:
                    hubo.append(j)
                    count += sascha.count(z)

    if hubo_ratio:
        print(hubo[hubo_ratio.index(max(hubo_ratio))])
    else:
        print(dictionary[0])
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

#포기;

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
#     sascha_word = list(sascha)
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
#     if hubo_ratio:
#         print(hubo[hubo_ratio.index(max(hubo_ratio))])
#     else:
#         print(dictionary[0])

def min_substitutions(word1, word2):
    """두 단어 간의 최소 대체 횟수를 계산하는 함수."""
    return sum(1 for a, b in zip(word1, word2) if a != b)


n = int(input())
for _ in range(n):
    sascha = input().strip()
    exam = int(input())
    dictionary = [input().strip() for _ in range(exam)]

    min_replacements = float('inf')
    most_likely_word = None

    for word in dictionary:
        # 대체 횟수 계산
        replacements = min_substitutions(sascha, word)

        if replacements < min_replacements:
            min_replacements = replacements
            most_likely_word = word
        elif replacements == min_replacements:
            # 사전에서 먼저 나오는 단어를 선택
            if most_likely_word is None or dictionary.index(word) < dictionary.index(most_likely_word):
                most_likely_word = word

    print(most_likely_word)

# 다른 사람 풀이
# for _ in range(int(input())):
#     sascha_word = input()
#     dictionary = [input() for _ in range(int(input()))]
#     min_substitutions = float('inf')
#     likely_word = ''
#
#     for word in dictionary:
#         substitutions = sum(a != b for a, b in zip(sascha_word, word))
#         if substitutions < min_substitutions:
#             min_substitutions = substitutions
#             likely_word = word
#
#     print(likely_word)
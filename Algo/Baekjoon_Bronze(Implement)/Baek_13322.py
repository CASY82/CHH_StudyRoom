# 이건 접미사 였다,,,
# import sys
#
# word = sys.stdin.readline().strip()
# length = len(word)
#
# array = []
#
# for i in range(length):
#     array.append((length - 1 - i, word[length - 1 - i:]))
#
# array.sort(key=lambda x: x[1])
#
# for num, word_impl in array:
#     print(num)

import sys

word = sys.stdin.readline().strip()
length = len(word)

for i in range(length):
    print(i)

# array = []
#
# for i in range(length):
#     array.append(word[:i + 1])
#
# print(array)
#
# array.sort()
#
# print(array)
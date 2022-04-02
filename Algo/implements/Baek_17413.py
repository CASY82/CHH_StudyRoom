import sys

Sentence = sys.stdin.readline().strip()
i = 0
stack = []
result = ''

while i <= len(Sentence):
    if i < len(Sentence):
        if Sentence[i] == "<":
            while stack:
                result += stack.pop()

            while Sentence[i] != ">":
                result += Sentence[i]
                i += 1
            result += ">"
            i += 1
        else:
            if Sentence[i] != " ":
                stack.append(Sentence[i])
                i += 1
            else:
                while stack:
                    result += stack.pop()

                result += " "
                i += 1
    else:
        while stack:
            result += stack.pop()

        i += 1

print(result)


# 다른 사람 풀이
# from collections import deque
#
# S = input()
# deq = deque()
#
# ans = ''
# is_in = False
# for a in S:
#     if a == '<':
#         while deq:
#             ans += deq.pop()
#         ans += '<'
#         is_in = True
#
#     elif a == '>':
#         while deq:
#             ans += deq.popleft()
#         ans += '>'
#         is_in = False
#
#     elif a == ' ' and not is_in:
#         while deq:
#             ans += deq.pop()
#         ans += ' '
#
#     else:
#         deq.append(a)
#
# while deq:
#     ans += deq.pop()
# print(ans)
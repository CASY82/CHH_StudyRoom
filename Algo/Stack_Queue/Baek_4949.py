import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    stack = []

    if sentence == '.':
        break

    for i in range(len(sentence)):
        if sentence[i] == '(' or sentence[i] == '[':
            stack.append(sentence[i])

        if sentence[i] == ')' or sentence[i] == ']':
            stack.append(sentence[i])

        if len(stack) >= 2:
            if stack[len(stack) - 2] == '(' and stack[len(stack) - 1] == ')':
                stack.pop()
                stack.pop()

            elif stack[len(stack) - 2] == '[' and stack[len(stack) - 1] == ']':
                stack.pop()
                stack.pop()

    if stack:
        print("no")
    else:
        print("yes")

#풀이 자체는 비슷하지만 -1 사용법을 알게되어서 첨부
# import sys
#
# str = sys.stdin.readline()
#
# while (str != '.\n'):
#     stack = []
#     for i in range(len(str) - 1):
#         if str[i] == '(' or str[i] == '[':
#             stack.append(str[i])
#         elif str[i] == ')':
#             if len(stack) == 0:
#                 stack.append(' ')
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#             else:
#                 break
#         elif str[i] == ']':
#             if len(stack) == 0:
#                 stack.append(' ')
#                 break
#             elif stack[-1] == '[':
#                 stack.pop()
#             else:
#                 break
#
#     if len(stack) == 0:
#         print('yes')
#     else:
#         print('no')
#
#     str = sys.stdin.readline()
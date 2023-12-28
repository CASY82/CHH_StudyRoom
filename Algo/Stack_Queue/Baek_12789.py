import sys

n = int(sys.stdin.readline())
student = list(map(int, sys.stdin.readline().split()))

now = 1
stack = []
point = 0

while len(student) != point:
    if student[point] == now:
        now += 1
        point += 1
    elif stack and stack[-1] == now:
        stack.pop()
        now += 1
    else:
        stack.append(student[point])
        point += 1

while stack:
    if stack[-1] == now:
        stack.pop()
        now += 1
    else:
        break

if stack:
    print("Sad")
else:
    print("Nice")

# 다른 사람 풀이
# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n = int(input())
#
# input_ = list(map(int, input().split()))
# stack = deque()
#
# num = 1
# while input_ or stack:
#     if input_:
#         if num == input_[0]:
#             input_.pop(0)
#             num += 1
#             continue
#     if stack:
#         if num == stack[-1]:
#             stack.pop()
#             num += 1
#             continue
#     if input_:
#         stack.append(input_.pop(0))
#
#     if not input_:
#         if num != stack[-1]:
#             break
#
# if not input_ and not stack:
#     print('Nice')
# else:
#     print('Sad')
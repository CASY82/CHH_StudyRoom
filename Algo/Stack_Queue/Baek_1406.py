# import sys
#
# word = list(sys.stdin.readline().strip())
# m = int(sys.stdin.readline())
# cursor = len(word)
# stack = []

# 시간 초과
# for _ in range(m):
#     comm = list(sys.stdin.readline().strip().split())
#
#     if comm[0] == 'L':
#         if cursor > 0:
#             cursor -= 1
#         else:
#             continue
#
#     if comm[0] == 'D':
#         if cursor < len(word):
#             cursor += 1
#         else:
#             continue
#
#     if comm[0] == 'B':
#         if cursor <= 0:
#             continue
#         else:
#             del word[cursor-1]
#             cursor -= 1
#
#     if comm[0] == 'P':
#         word.insert(cursor, comm[1])
#         cursor += 1
#
#     print(word)
#
# print(''.join(word))

import sys

word = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
tmp = []
stack = word.copy()

for _ in range(m):
    comm = list(sys.stdin.readline().strip().split())

    if comm[0] == 'L':
        if stack:
            tmp.append(stack.pop())
        else:
            continue

    if comm[0] == 'D':
        if tmp:
            stack.append(tmp.pop())
        else:
            continue

    if comm[0] == 'B':
        if stack:
            stack.pop()
        else:
            continue

    if comm[0] == 'P':
        stack.append(comm[1])

while tmp:
    stack.append(tmp.pop())

print(''.join(stack))
import sys

s = set()
n = int(sys.stdin.readline())

for _ in range(n):
    command = list(sys.stdin.readline().split())

    if command[0] == 'add':
        s.add(int(command[1]))

    if command[0] == 'check':
        if int(command[1]) in s:
            print(1)
        else:
            print(0)

    if command[0] == 'remove':
        s.discard(int(command[1]))

    if command[0] == 'toggle':
        if int(command[1]) in s:
            s.discard(int(command[1]))
        else:
            s.add(int(command[1]))

    if command[0] == 'all':
        s = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    if command[0] == 'empty':
        s.clear()


#본래의 비트마스킹을 이용하는 방법
# import sys
#
# test_case = int(sys.stdin.readline())
#
# s = 0b0
# all_s = 0b111111111111111111111
# not_s = 0b000000000000000000000
#
# for _ in range(test_case):
#     cmd = sys.stdin.readline().rstrip().split(' ')
#     if cmd[0] == 'add':
#         s = s | (1 << int(cmd[-1]))
#     elif cmd[0] == 'remove':
#         s = s & ~(1 << int(cmd[-1]))
#     elif cmd[0] == 'check':
#         if s & (1 << int(cmd[-1])):
#             print(1)
#         else:
#             print(0)
#     elif cmd[0] == 'toggle':
#         s = s ^ (1 << int(cmd[-1]))
#     elif cmd[0] == 'all':
#         s = all_s
#     elif cmd[0] == 'empty':
#         s = not_s
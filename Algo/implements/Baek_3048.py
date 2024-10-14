# import sys
#
# n1, n2 = map(int, sys.stdin.readline().split())
# n1_str = sys.stdin.readline().strip()
# n2_str = sys.stdin.readline().strip()
# t = int(sys.stdin.readline())
# case = 0
# switch_phase = 0
#
# reverse_n1_str = n1_str[::-1]
# init_str = list(reverse_n1_str + n2_str)
#
# def switchArray(array, index1, index2):
#     if index1 >= len(array) or index1 < 0 or index2 >= len(array) or index2 < 0:
#         return
#
#     array[index1], array[index2] = array[index2], array[index1]
#
# while case < t:
#     middle = len(n1_str)
#
#     if switch_phase == 0:
#         switchArray(init_str, middle, middle - 1)
#     else:
#         for i in range(0, switch_phase * 2 + 1, 2):
#             switchArray(init_str, middle - case + i, middle - case - 1 + i)
#
#     case += 1
#     switch_phase += 1
#
# print("".join(init_str))
#

import sys

n1, n2 = map(int, sys.stdin.readline().split())
n1_str = sys.stdin.readline().strip()
n2_str = sys.stdin.readline().strip()
t = int(sys.stdin.readline())

reverse_n1_str = n1_str[::-1]
init_str = list(reverse_n1_str + n2_str)

for _ in range(t):
    for i in range(len(init_str) - 1):
        if init_str[i] in n1_str and init_str[i + 1] in n2_str:
            init_str[i], init_str[i + 1] = init_str[i + 1], init_str[i]

            if init_str[i + 1] == reverse_n1_str[-1]:
                break

print("".join(init_str))
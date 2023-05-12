# import sys
#
# a, b, c, need = map(int, sys.stdin.readline().split())
#
# num_list = [a, b, c, a + b, b + c, c + a, a + b + c]
#
# for i in range(len(num_list)):
#     for j in range(len(num_list)):
#         for k in range(len(num_list)):
#             if (need % num_list[i]) % num_list[j] % num_list[k] == 0:
#                 print(1)
#                 exit()
#
# print(0)

import sys

a, b, c, need = map(int, sys.stdin.readline().split())
tmp_a = need // a
tmp_b = need // b
tmp_c = need // c

for i in range(tmp_a+1):
    for j in range(tmp_b+1):
        for k in range(tmp_c+1):
            if i * a + j * b + k * c == need:
                print(1)
                exit()

print(0)
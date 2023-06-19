# import sys

# susic = sys.stdin.readline().strip()
# susic_arr = list(susic.split())
#
# num1 = int(susic[0])
# num2 = 0
# oper = ''
#
# for i in range(len(susic_arr)):
#     if susic_arr[i] in ('+', '-', '/', '*'):
#         oper = susic_arr[i]
#     else:
#         num2 = int(susic_arr[i])
#         if oper != '':
#             num1 = eval(str(num1) + oper + str(num2))
#
# result1 = int(eval(susic))
# result2 = num1
#
# print(min(result1, result2))
# print(max(result1, result2))

import sys

K1, O1, K2, O2, K3 = sys.stdin.readline().split()

result1 = 0
result2 = 0

result1 = int(eval(str(int(eval(K1 + O1 + K2))) + O2 + K3))
result2 = int(eval(K1 + O1 + str(int(eval(K2 + O2 + K3)))))

print(min(result1, result2))
print(max(result1, result2))
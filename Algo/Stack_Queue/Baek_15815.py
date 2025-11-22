# import sys
#
# susic = sys.stdin.readline().strip()
# op_list = ["*", "/", "+", "-"]
# op = []
# num = []
# res = 0
# res = ""
#
# for i in range(len(susic) - 1, -1, -1):
#     if susic[i] in op_list:
#         op.append(susic[i])
#     else:
#         num.append(susic[i])
#
#     if len(num) == 2:
#         fir = num.pop()
#         t_op = op.pop()
#         sec = num.pop()
#         res = str(eval(fir + t_op + sec))
#
#         num.append(res)
#
# print(res)

import sys

expr = sys.stdin.readline().strip()
stack = []

for ch in expr:
    if ch.isdigit():  # 피연산자 (0~9)
        stack.append(int(ch))
    else:  # 연산자
        b = stack.pop()  # 오른쪽 피연산자
        a = stack.pop()  # 왼쪽 피연산자

        if ch == '+':
            stack.append(a + b)
        elif ch == '-':
            stack.append(a - b)
        elif ch == '*':
            stack.append(a * b)
        elif ch == '/':
            stack.append(int(a / b))

print(stack[0])

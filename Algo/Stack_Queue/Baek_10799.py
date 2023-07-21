import sys

iron_pipe = sys.stdin.readline().strip()

stack = []
pipe_cnt = 0
result = 0

for i in range(len(iron_pipe)):
    stack.append(iron_pipe[i])

    if stack[-1] == "(":
        pipe_cnt += 1
        result += 1

    if stack[-1] == ")":
        if stack[-2] == "(":
            pipe_cnt -= 1
            result -= 1
            result += pipe_cnt
        else:
            pipe_cnt -= 1

    # print("? : ", pipe_cnt, "result : ", result)

print(result)

# import sys
# input = __import__('sys').stdin.readline
#
# def main():
#     string = input().rstrip()
#     st = []
#     res = 0
#
#     for i,ch in  enumerate(string):
#         if ch == '(':
#             st.append(ch)
#         else:
#             if string[i - 1] == '(':
#                 st.pop()
#                 res += len(st)
#             else:
#                 st.pop()
#                 res += 1
#
#     print(res)
#
#
#
#
# if __name__ == "__main__":
#     main()
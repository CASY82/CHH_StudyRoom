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
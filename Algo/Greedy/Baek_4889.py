import sys

num = 1

while True:
    stable_string = sys.stdin.readline().strip()

    if "-" in stable_string:
        break

    stack = []

    for i in range(len(stable_string)):
        stack.append(stable_string[i])
        if len(stack) >= 2 and stack[-2] == "{" and stack[-1] == "}":
            stack.pop()
            stack.pop()

    cnt = 0

    if len(stack) % 2 == 1:
        cnt += 1
        stack.pop()

    for i in range(len(stack)):
        if i % 2 == 0:
            if stack[i] == "}":
                cnt += 1

        if i % 2 == 1:
            if stack[i] == "{":
                cnt += 1

    print("{0}. {1}".format(num, cnt))
    num += 1
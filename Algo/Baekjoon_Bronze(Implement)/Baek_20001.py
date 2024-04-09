import sys
stack = []

while True:
    duck = list(sys.stdin.readline().strip().split())

    if len(duck) >= 2:
        if duck[2] == "시작":
            continue

        if duck[2] == "끝":
            break

    if len(stack) == 0 and duck[0] == "고무오리":
        stack.append("문제")
        stack.append("문제")
    else:
        if len(stack) > 0 and stack[-1] == "문제":
            if duck[0] == "고무오리":
                stack.pop()
            else:
                stack.append(duck[0])
        else:
            stack.append(duck[0])


if len(stack) == 0:
    print("고무오리야 사랑해")
else:
    print("힝구")

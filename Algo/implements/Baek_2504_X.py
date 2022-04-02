# 문자열 + 구현이 정말 큰 약점인듯 많이 풀어봐야할 필요성이 있다.
import sys

bracket = sys.stdin.readline().strip()
stack = []
result = 0
# 임시 변수를 사용해서 풀면된다니...
tmp = 1

for i in range(len(bracket)):
    if bracket[i] == "(":
        stack.append(bracket[i])
        tmp *= 2

    elif bracket[i] == "[":
        stack.append(bracket[i])
        tmp *= 3

    elif bracket[i] == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        # 몇번을 곱하게 되든 결국 여기서는 더하게 된다.
        # 즉 1번만 나왔으면 정직하게 2를 더하는거고 여러번 나왔으면 그 계산이 더해지게 될것
        if bracket[i-1] == "(":
            result += tmp

        stack.pop()
        tmp //= 2

    elif bracket[i] == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break

        if bracket[i-1] == "[":
            result += tmp

        stack.pop()
        tmp //= 3

# 스택이 안비어있다면 문자열이 잘못되어있다!!
if stack:
    print(0)
else:
    print(result)
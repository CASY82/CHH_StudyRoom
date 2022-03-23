import sys

n = int(sys.stdin.readline())
cnt = 0
stack = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if stack and stack[-1] < num:
        while stack and stack[-1] < num:
            stack.pop()
        stack.append(num)
    else:
        stack.append(num)

print(len(set(stack)))
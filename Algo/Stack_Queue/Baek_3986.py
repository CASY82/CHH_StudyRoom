import sys

n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    stack = []
    word = sys.stdin.readline().strip()

    for i in word:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        cnt += 1

print(cnt)
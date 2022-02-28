import sys

n, k = map(int, sys.stdin.readline().split())
num = list(sys.stdin.readline().strip())
stack = []
cnt = 0

for i in range(len(num)):
    stack.append(num[i])

    if i < len(num)-1:
        while stack:
            if stack[-1] < num[i+1]:
                stack.pop()
                cnt += 1
                if cnt == k:
                    break
            else:
                break
    else:
        if cnt < k:
            while cnt < k:
                stack.pop()
                cnt += 1

    if cnt == k:
        break

stack += num[i + 1:]

print(''.join(stack))
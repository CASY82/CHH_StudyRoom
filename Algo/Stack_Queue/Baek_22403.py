import sys

n = int(sys.stdin.readline())
stack = []
res = True

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == "A":
        stack.append(command)
    else:
        if len(stack) > 0:
            stack.pop()
        else:
            res = False
            break

if res and len(stack) == 0:
    print("YES")
else:
    print("NO")
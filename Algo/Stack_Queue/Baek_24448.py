import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    command = sys.stdin.readline().strip()

    if command == "READ":
        print(stack.pop())
    else:
        stack.append(command)
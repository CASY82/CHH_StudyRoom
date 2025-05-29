import sys

n = int(sys.stdin.readline())
ingredients = list(sys.stdin.readline().strip().split())
used = set(sys.stdin.readline().strip().split())

for item in ingredients:
    if item not in used:
        print(item)
        break
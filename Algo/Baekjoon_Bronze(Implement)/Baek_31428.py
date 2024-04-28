import sys

n = int(sys.stdin.readline())
friends = list(sys.stdin.readline().strip().split())
me = sys.stdin.readline().strip()

result = 0

for track in friends:
    if track == me:
        result += 1

print(result)
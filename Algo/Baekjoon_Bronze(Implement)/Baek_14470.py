import sys

meet_degree = int(sys.stdin.readline())
target_degree = int(sys.stdin.readline())
heatup = int(sys.stdin.readline())
meltheattime = int(sys.stdin.readline())
nonmeltheattime = int(sys.stdin.readline())

result = 0
freeze = False

if meet_degree < 0:
    result += abs(meet_degree) * heatup
    meet_degree = 0
    freeze = True

if meet_degree == 0 and freeze:
    result += meltheattime

result += (target_degree - meet_degree) * nonmeltheattime

print(result)
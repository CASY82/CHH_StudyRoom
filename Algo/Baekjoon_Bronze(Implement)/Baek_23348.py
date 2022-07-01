import sys

one_hand, no_look, phone = map(int, sys.stdin.readline().split())

n = int(sys.stdin.readline())

team = []
result = 0

for i in range(1, n * 3 + 1):
    a, b, c = map(int, sys.stdin.readline().split())

    tmp = a * one_hand + no_look * b + c * phone
    result += tmp

    if i % 3 == 0:
        team.append(result)
        result = 0

team.sort()
print(team[-1])
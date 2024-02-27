import sys

t = int(sys.stdin.readline())

for _ in range(t):
    vote = int(sys.stdin.readline())

    result = ""

    five = vote // 5
    remain = vote % 5

    for i in range(five):
        result += "++++ "

    for j in range(remain):
        result += "|"

    print(result.rstrip())
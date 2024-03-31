import sys

t = int(sys.stdin.readline())

for i in range(t):
    rank = int(sys.stdin.readline())

    result = "Case #{0}: "

    if rank <= 25:
        result += "World Finals"
    elif rank <= 1000:
        result += "Round 3"
    elif rank <= 4500:
        result += "Round 2"
    else:
        result += "Round 1"

    print(result.format(i + 1))
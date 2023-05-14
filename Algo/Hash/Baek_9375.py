import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    wearing = dict()
    result = 1

    for _ in range(n):
        name, category = sys.stdin.readline().strip().split()

        if category not in wearing:
            wearing[category] = 1
        else:
            wearing[category] += 1

    val = list(wearing.values())
    # 모든 경우에서 +1 해주면 안입는 경우도 고르는 것이 된다.
    for i in range(len(val)):
        result *= (val[i] + 1)

    # 그런데 모두 안입는 경우는 빼야되니까 -1
    print(result-1)
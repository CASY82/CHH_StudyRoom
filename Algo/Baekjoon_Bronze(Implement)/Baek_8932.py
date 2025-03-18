import sys

t = int(sys.stdin.readline())
rules = [
    [9.23076, 26.7, 1.835],
    [1.84523, 75, 1.348],
    [56.0211, 1.5, 1.05],
    [4.99087, 42.5, 1.81],
    [0.188807, 210, 1.41],
    [15.9803, 3.8, 1.04],
    [0.11193, 254, 1.88]
]


for _ in range(t):
    get_score = list(map(int, sys.stdin.readline().split()))
    res = 0

    for i in range(7):
        if i in [0, 3, 6]:
            res += int(rules[i][0] * (rules[i][1] - get_score[i]) ** rules[i][2])
        else:
            res += int(rules[i][0] * (get_score[i] - rules[i][1]) ** rules[i][2])

    print(res)
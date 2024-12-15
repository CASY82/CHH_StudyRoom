import sys

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    text = []
    res = 0

    for _ in range(n):
        text.append(list((sys.stdin.readline().rstrip())))

    for index, word in enumerate(text[0]):
        if word != " ":
            res = index + 1
            break

    for i in range(n):
        if len(text[i]) < res:
            continue

        for j in range(max(res - 1, 0), len(text[i])):
            if text[i][j] == " ":
                res = j + 1
                break

            if j == len(text[i]) - 1:
                res = len(text[i]) + 1
                break

    print(res)
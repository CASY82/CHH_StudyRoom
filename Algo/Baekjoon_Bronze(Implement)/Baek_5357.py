import sys

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().strip()
    result = []

    result.append(word[0])
    tmp = word[0]
    for i in range(1, len(word)):
        if tmp == word[i]:
            continue
        else:
            result.append(word[i])
            tmp = word[i]

    for i in range(len(result)):
        print(result[i], end="")

    print()
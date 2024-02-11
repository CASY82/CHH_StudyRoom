import sys

word = sys.stdin.readline().strip()

for i in range(len(word)):
    tmp = str(ord(word[i]))

    if len(tmp) == 3:
        length = int(tmp[0]) + int(tmp[1]) + int(tmp[2])
    else:
        length = int(tmp[0]) + int(tmp[1])

    for j in range(length):
        print(word[i], end="")

    print()
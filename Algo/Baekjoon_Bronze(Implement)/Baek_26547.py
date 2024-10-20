import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = sys.stdin.readline().strip()
    length = len(word)
    reverse_word = word[::-1]

    array = [[" " for _ in range(length)] for _ in range(length)]

    # 맨 윗줄
    for i in range(length):
        array[0][i] = word[i]

    # 왼쪽
    for j in range(length):
        array[j][0] = word[j]

    # 오른쪽
    for k in range(length):
        array[k][-1] = reverse_word[k]

    # 맨 아래
    for l in range(length):
        array[-1][l] = reverse_word[l]

    for level in range(length):
        print("".join(array[level]))
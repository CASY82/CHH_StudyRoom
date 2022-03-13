import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = input()

    length = int(len(word) ** 0.5)
    word_array = [["" for i in range(length)] for j in range(length)]

    word_cnt = 0
    for i in range(length):
        for j in range(length-1, -1, -1):
            word_array[j][i] = word[word_cnt]
            word_cnt += 1

    for i in range(length):
        for j in range(length):
            print(word_array[i][j], end="")

    print()
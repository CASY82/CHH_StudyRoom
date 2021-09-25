interpret = ['-', '\\', '(', '@', '?', '>', '&', '%', '/']

while True:
    result = 0
    word = input()

    if word == '#':
        break

    for i in range(len(word)):
        for j in range(len(interpret)):
            if word[i] == interpret[j]:
                if j == 8:
                    result += (8 ** (len(word) - 1 - i)) * (-1)
                    # print(i, j, len(word), result)
                else:
                    result += (8 ** (len(word) - 1 - i)) * j
                    # print(i, j, len(word), result)

    print(result)

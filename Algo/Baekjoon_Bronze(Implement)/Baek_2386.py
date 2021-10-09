while True:
    word = []
    word = input().split()
    result = 0

    if word[0] == '#':
        break

    for i in range(1, len(word)):
        word[i] = word[i].lower()
        result += word[i].count(word[0])

    print(word[0], result)
from builtins import EOFError

while True:
    try:
        word = input()
    except EOFError:
        break

    word = list(word)
    count = [0] * 4

    for i in range(len(word)):
        if ord('a') <= ord(word[i]) <= ord('z'):
            count[0] += 1
        elif ord('A') <= ord(word[i]) <= ord('Z'):
            count[1] += 1
        elif ord('0') <= ord(word[i]) <= ord('9'):
            count[2] += 1
        elif word[i] == " ":
            count[3] += 1

    for i in count:
        print(i, end=' ')
    print()
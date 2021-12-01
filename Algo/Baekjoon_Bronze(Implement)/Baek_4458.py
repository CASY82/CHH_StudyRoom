n = int(input())

for _ in range(n):
    word = input()

    word = list(word)

    if ord(word[0]) > 91:
        word[0] = chr(ord(word[0]) - 32)

    print(''.join(word))
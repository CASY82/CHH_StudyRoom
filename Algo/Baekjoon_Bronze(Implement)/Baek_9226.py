import sys

vowels = "a e i o u".split()

while True:
    word = list(sys.stdin.readline().strip())

    if word[0] == "#":
        break

    length = len(word)
    cnt = 0

    while True:
        if cnt != length:
            if word[0] not in vowels:
                word.append(word.pop(0))
                cnt += 1
            else:
                break
        else:
            break

    tmp = "".join(word) + "ay"

    print(tmp)
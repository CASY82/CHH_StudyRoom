import sys

while True:
    word = list(sys.stdin.readline().strip())

    if ''.join(word) == "END":
        break

    word.reverse()

    print(''.join(word))
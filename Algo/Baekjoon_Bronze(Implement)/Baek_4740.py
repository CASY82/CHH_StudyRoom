import sys

while True:
    word = sys.stdin.readline().rstrip('\n')

    if word == "***":
        break

    print("".join(list(reversed(word))))
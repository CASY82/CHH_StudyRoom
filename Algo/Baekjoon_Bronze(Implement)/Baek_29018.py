import sys

while True:
    s = sys.stdin.readline().strip()

    if s == "#":
        break

    small = []
    big = []
    num = []

    for i in range(len(s)):
        tmp = ord(s[i])

        if 65 <= tmp <= 90:
            big.append(s[i])
        elif 97 <= tmp <= 122:
            small.append(s[i])
        else:
            num.append(s[i])

    small.sort()
    big.sort()
    num.sort()

    print("".join(small + big + num))
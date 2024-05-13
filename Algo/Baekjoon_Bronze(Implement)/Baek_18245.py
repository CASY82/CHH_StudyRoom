import sys

i = 1

while True:
    crypt = sys.stdin.readline().strip()

    if crypt == "Was it a cat I saw?":
        break

    decrypt = ""

    for point in range(0, len(crypt),i + 1):
        decrypt += crypt[point]

    i += 1

    print(decrypt)
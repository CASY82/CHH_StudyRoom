import sys

alpha = [" ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

while True:
    sentence = sys.stdin.readline().strip()
    result = 0

    if sentence == "#":
        break

    for i in range(len(sentence)):
        result += alpha.index(sentence[i]) * (i+1)

    print(result)
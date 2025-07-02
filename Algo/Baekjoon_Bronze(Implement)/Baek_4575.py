import sys

res = []

while True:
    sentence = sys.stdin.readline().strip()

    if sentence == "END":
        break

    alpha = set()
    check = True

    for i in range(len(sentence)):
        if sentence[i] != " ":
            if sentence[i] not in alpha:
                alpha.add(sentence[i])
            else:
                check = False
                break

    if check:
        res.append(sentence)

for ans in res:
    print(ans)
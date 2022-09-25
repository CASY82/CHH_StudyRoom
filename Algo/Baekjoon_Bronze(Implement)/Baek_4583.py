import sys

rev_mirror = ["b", "d", "p", "q"]
self_mirror = ["i", "o", "v", "w", "x"]

while True:
    word = sys.stdin.readline().strip()
    tmp = True

    new_word = []

    if word == "#":
        break

    for check in range(len(word)):
        if word[check] not in rev_mirror and word[check] not in self_mirror:
            tmp = False
            break
        else:
            if word[check] == "b":
                new_word.append("d")
            elif word[check] == "p":
                new_word.append("q")
            elif word[check] == "d":
                new_word.append("b")
            elif word[check] == "q":
                new_word.append("p")
            else:
                new_word.append(word[check])

    if tmp:
        new_word.reverse()
        print("".join(new_word))
    else:
        print("INVALID")
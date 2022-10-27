import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word = sys.stdin.readline().strip()
    check = dict()
    result = True
    i = 0

    while i < len(word):
        if word[i] in check:
            check[word[i]] += 1
            if check[word[i]] == 3:
                check[word[i]] = 0
                if i+1 >= len(word) or word[i] != word[i+1]:
                    result = False
                    break
                i += 1
        else:
            check[word[i]] = 1

        i += 1

    if result:
        print("OK")
    else:
        print("FAKE")
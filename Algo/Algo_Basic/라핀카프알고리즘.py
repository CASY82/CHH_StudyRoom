def findString(parent, pattern):
    parentSize = len(parent)
    patternSize = len(pattern)
    parentHash = 0
    patternHash = 0
    power = 1

    for i in range(parentSize - patternSize + 1):
        if i == 0:
            for j in range(patternSize):
                parentHash += ord(parent[patternSize - 1 - j]) * power
                patternHash += ord(pattern[patternSize - 1 - j]) * power
                if j < patternSize - 1 :
                    power *= 2
        else:
            parentHash = 2 * (parentHash - ord(parent[i - 1]) * power) + ord(parent[patternSize - 1 + i])

        if parentHash == patternHash:
            check = True
            for k in range(patternSize):
                if parent[i + k] != pattern[k]:
                    check = False

            if check:
                print(i + 1, "번째에서 발견")

parent = "ababacabacaabacaaba"
pattern = "abacaaba"
findString(parent, pattern)
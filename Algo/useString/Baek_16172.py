import sys

def makeTable(pattern):
    patternSize = len(pattern)
    table = [0 for _ in range(patternSize)]
    j = 0

    for i in range(1, patternSize):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j

    return table

def kmp(parent, pattern):
    table = makeTable(pattern)
    parentSize = len(parent)
    patternSize = len(pattern)
    j = 0

    for i in range(parentSize):
        if ord('0') <= ord(parent[i]) <= ord('9'):
            continue
        else:
            while j > 0 and parent[i] != pattern[j]:
                j = table[j - 1]

            if parent[i] == pattern[j]:
                if j == patternSize - 1:
                    return True
                else:
                    j += 1

    return False

parent = sys.stdin.readline().strip()
pattern = sys.stdin.readline().strip()

if kmp(parent, pattern):
    print(1)
else:
    print(0)
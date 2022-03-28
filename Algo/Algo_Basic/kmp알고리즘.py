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
    parentSize = len(parent)
    patternSize = len(pattern)
    table = makeTable(pattern)
    j = 0

    for i in range(parentSize):
        while j > 0 and parent[i] != pattern[j]:
            j = table[j - 1]

        if parent[i] == pattern[j]:
            if j == patternSize - 1:
                #여기서 값을 찍으면 됨
                return True
            else:
                j += 1

    return False
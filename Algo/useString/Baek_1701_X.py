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

pattern = sys.stdin.readline().strip()
result = 0

for i in range(len(pattern)):
    # 생각해보니 앞에서부터 자르면 된다. 왜냐하면 어차피 중간에서 자른것도 makeTable쪽에서 걸러주므로
    sub_pattern = pattern[i:len(pattern)]
    result = max(result, max(makeTable(sub_pattern)))

print(result)

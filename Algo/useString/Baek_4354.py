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

while True:
    pattern = sys.stdin.readline().strip()

    if pattern == ".":
        break

    result = makeTable(pattern)
    # 이 부분을 이상하게 구현하고 있었음... 그래서 2번 틀림
    # 패턴이 반복되고 있으므로 result의 마지막 값을 이용해서 전체 길이에서 빼면 반복하는 패턴의 길이를 구할 수 있다.
    # 반복되는 패턴의 길이를 이용해서 문제를 풀었어야 했음
    tmp = len(pattern) - result[len(pattern)-1]
    if len(pattern) % tmp == 0:
        print(len(pattern) // tmp)
    else:
        print(1)
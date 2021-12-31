import sys

n = int(sys.stdin.readline())
wordList = []
length = []
pairList = []

# 1. 길이 짧은거
# 2. 사전 순(숫자가 뒤로 가야됨)
# 3. 마지막으로 사전순

for _ in range(n):
    wordList.append(sys.stdin.readline().strip())

for i in range(len(wordList)):
    numSum = 0
    for j in range(len(wordList[i])):
        if ord('0') <= ord(wordList[i][j]) <= ord('9'):
            numSum += int(wordList[i][j])

    length.append(numSum)

for pair in zip(length, wordList):
    pairList.append(list(pair))

pairList.sort(key = lambda x : (len(x[1]), x[0], x[1]))

for v, i in pairList:
    print(i)
import sys

while True:
    n = int(sys.stdin.readline())
    wordList = dict()

    if n == 0:
        break

    for _ in range(n):
        word = sys.stdin.readline().strip()

        wordList[word] = word.upper()


    sort_dict = sorted(wordList.items(), key = lambda item: item[1])

    print(sort_dict[0][0])
import sys

n, m = map(int, sys.stdin.readline().split())

word_paper = dict()

for _ in range(n):
    word = sys.stdin.readline().strip()

    if len(word) < m:
        continue

    if word not in word_paper:
        word_paper[word] = 1
    else:
        word_paper[word] += 1

tmp = sorted(word_paper.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for result in tmp:
    print(result[0])

